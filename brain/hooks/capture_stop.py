#!/usr/bin/env python3
"""Stop + SubagentStop hook. The payload carries no assistant text, only a
pointer, so this opens the transcript and reads ONLY the bytes appended since the
last turn (per-session byte-offset watermark), then appends Claude's final text
blocks. Transcripts run large (tens to ~120 MB), so reading byte-incrementally is
what keeps this fast. Thinking blocks are redacted in the transcript and cannot be
captured. Prints NOTHING. Fails silent."""
import sys, os, json, datetime

CAP = os.path.expanduser("~/.claude/capture")
RAW = os.path.join(CAP, "raw")
WM = os.path.join(CAP, ".watermark.json")


def load_wm():
    try:
        with open(WM, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_wm(d):
    try:
        with open(WM, "w", encoding="utf-8") as f:
            json.dump(d, f)
        os.chmod(WM, 0o600)
    except Exception:
        pass


def text_blocks(entry):
    msg = entry.get("message")
    if not isinstance(msg, dict):
        return []
    content = msg.get("content")
    if isinstance(content, str):
        return [content] if content.strip() else []
    out = []
    if isinstance(content, list):
        for b in content:
            if isinstance(b, dict) and b.get("type") == "text":
                t = b.get("text", "")
                if t and t.strip():
                    out.append(t)
    return out


def main():
    if os.environ.get("CLAUDE_CAPTURE_DISABLE"):
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tpath = data.get("transcript_path", "")
    sess = data.get("session_id", "")
    if not tpath or not os.path.exists(tpath):
        return
    try:
        wm = load_wm()
        prev = wm.get(sess, {})
        offset = prev.get("offset", 0) if prev.get("path") == tpath else 0
        size = os.path.getsize(tpath)
        if offset > size:      # file was rewritten/shrank (e.g. compaction)
            offset = 0
        if offset == size:     # nothing new
            return
        with open(tpath, "rb") as f:
            f.seek(offset)
            raw = f.read()
        cut = raw.rfind(b"\n")          # only process up to the last complete line
        if cut == -1:
            return
        chunk = raw[:cut + 1].decode("utf-8", "replace")
        new_offset = offset + cut + 1

        now = datetime.datetime.now()
        os.makedirs(RAW, exist_ok=True)
        path = os.path.join(RAW, now.strftime("%Y-%m-%d") + ".jsonl")
        # Dedup guard for interruption text: a manual backfill (or a re-read after compaction) can already
        # hold a queue-operation's text, and the same op fires enqueue+remove. Load today's existing human
        # texts once and skip any interrupt already present. Assistant text is not deduped (long and unique).
        seen_human = set()
        if os.path.exists(path):
            try:
                for _l in open(path, encoding="utf-8"):
                    try:
                        _r = json.loads(_l)
                    except Exception:
                        continue
                    if _r.get("role") == "human":
                        seen_human.add(" ".join((_r.get("text") or "").split()))
            except Exception:
                pass
        with open(path, "a", encoding="utf-8") as out:
            for line in chunk.splitlines():
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                except Exception:
                    continue
                et = entry.get("type")
                # the human's MID-TURN interruptions never reach the UserPromptSubmit hook: the CLI stores them as
                # queue-operation "enqueue" entries, not as user messages. Capture their verbatim content here
                # so an interruption is never dropped (fixed 2026-07-24 after several were lost). The paired
                # "remove" op repeats the same text, so only "enqueue" is taken.
                if et == "queue-operation" and entry.get("operation") == "enqueue":
                    c = entry.get("content")
                    if isinstance(c, str) and c.strip() and " ".join(c.split()) not in seen_human:
                        seen_human.add(" ".join(c.split()))
                        rec = {
                            "ts": entry.get("timestamp", now.strftime("%Y-%m-%dT%H:%M:%S"))[:19],
                            "session": sess,
                            "role": "human",
                            "type": "prompt-interrupt",
                            "text": c,
                        }
                        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    continue
                if et != "assistant":
                    continue
                role = "subagent" if entry.get("isSidechain") else "claude"
                for t in text_blocks(entry):
                    rec = {
                        "ts": entry.get("timestamp", now.strftime("%Y-%m-%dT%H:%M:%S")),
                        "session": sess,
                        "role": role,
                        "type": "text",
                        "text": t,
                    }
                    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        try:
            os.chmod(path, 0o600)
        except Exception:
            pass
        wm[sess] = {"path": tpath, "offset": new_offset}
        save_wm(wm)
    except Exception:
        pass


if __name__ == "__main__":
    main()

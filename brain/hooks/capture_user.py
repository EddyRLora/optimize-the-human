#!/usr/bin/env python3
"""UserPromptSubmit hook. Appends the human's verbatim prompt to the raw log.
Prints NOTHING (stdout on UserPromptSubmit is injected into the model context).
Fails silent: a capture error must never disrupt a session."""
import sys, os, json, datetime

CAP = os.path.expanduser("~/.claude/capture")
RAW = os.path.join(CAP, "raw")


def main():
    if os.environ.get("CLAUDE_CAPTURE_DISABLE"):
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    try:
        prompt = data.get("prompt", "")
        if not prompt or not prompt.strip():
            return
        os.makedirs(RAW, exist_ok=True)
        now = datetime.datetime.now()
        rec = {
            "ts": now.strftime("%Y-%m-%dT%H:%M:%S"),
            "session": data.get("session_id", ""),
            "role": "human",
            "type": "prompt",
            "text": prompt,
            "cwd": data.get("cwd", ""),
        }
        path = os.path.join(RAW, now.strftime("%Y-%m-%d") + ".jsonl")
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        try:
            os.chmod(path, 0o600)
        except Exception:
            pass
    except Exception:
        pass


if __name__ == "__main__":
    main()

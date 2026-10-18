#!/usr/bin/env python3
"""PostToolUse hook (all tools). Appends a bounded record of what Claude DID.
Replaces the old broken action-log hook (it parsed $CLAUDE_TOOL_INPUT, which is
not populated, so it logged 'command logged' for everything).
Prints NOTHING. Fails silent."""
import sys, os, json, datetime

CAP = os.path.expanduser("~/.claude/capture")
RAW = os.path.join(CAP, "raw")


def summarize_input(tool, ti):
    if not isinstance(ti, dict):
        return str(ti)[:600]
    if tool == "Bash":
        return ("$ " + str(ti.get("command", "")))[:600]
    if tool in ("Edit", "Write", "Read", "NotebookEdit", "MultiEdit"):
        return str(ti.get("file_path", ""))[:400]
    try:
        return json.dumps(ti, ensure_ascii=False)[:600]
    except Exception:
        return str(ti)[:600]


def main():
    if os.environ.get("CLAUDE_CAPTURE_DISABLE"):
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    try:
        tool = data.get("tool_name", "")
        if not tool:
            return
        os.makedirs(RAW, exist_ok=True)
        now = datetime.datetime.now()
        try:
            out = json.dumps(data.get("tool_response", ""), ensure_ascii=False)[:300]
        except Exception:
            out = str(data.get("tool_response", ""))[:300]
        rec = {
            "ts": now.strftime("%Y-%m-%dT%H:%M:%S"),
            "session": data.get("session_id", ""),
            "role": "claude",
            "type": "tool",
            "tool": tool,
            "input": summarize_input(tool, data.get("tool_input", {})),
            "result": out,
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

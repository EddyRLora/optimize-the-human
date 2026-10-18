#!/usr/bin/env python3
"""SessionStart hook. Prints what a cold session cannot infer: the heartbeat tail
(what other sessions changed) and the top of OPERATOR.md (who it is working with).
Set BRAIN_DIR if the vault is not at ~/brain. Prints nothing on any error, so a
hook failure can never block a session."""
import os
from pathlib import Path
V = Path(os.environ.get("BRAIN_DIR", Path.home() / "brain"))
def tail(p, n):
    try:
        lines = p.read_text(errors="ignore").splitlines()
        return "\n".join(lines[-n:])
    except Exception:
        return ""
def head(p, n):
    try:
        return "\n".join(p.read_text(errors="ignore").splitlines()[:n])
    except Exception:
        return ""
out = []
out.append("=== BOOT === Read in order before acting: CLAUDE.md, OS/Manual/Start Here.md, this heartbeat tail, "
           "the last 2 Conversation Log entries, OPERATOR.md. The reply rule: do the work whole, then the reasoning in prose. "
           "Log choices to this session's DECISIONS.md as you make them; a correction gets a gap entry with MY REASONING. ===")
hb = tail(V / "OS/Manual/HEARTBEAT.md", 15)
if hb:
    out.append("=== HEARTBEAT (what other sessions changed, newest last) ===\n" + hb)
op = head(V / "OPERATOR.md", 25)
if op:
    out.append("=== OPERATOR (the human, not the machine) ===\n" + op)
else:
    out.append("=== OPERATOR.md missing: run /audit ===")
print("\n".join(out))

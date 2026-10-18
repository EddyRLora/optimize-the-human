# 08 Parallel Sessions and the Heartbeat
> Up: [[00 - Index|Agent SOPs]]

**Why.** Four sessions ran in parallel. One handed the human a rundown wrong in nine places, off a picture loaded the night before, while every correction already sat on disk. The information was never the problem. Confidence does not decay when facts do. Something has to force the re-read.

**The heartbeat.** `OS/Manual/HEARTBEAT.md`, one line per material fact change, written by whichever session made it, append only, newest at the bottom. The SessionStart hook prints the tail into every session.

**Two rules.**
1. Before stating a fact outside your own lane (money, status, dates, gates, who owns what), read the tail.
2. When you change a fact another session would quote, append a line before you reply. Sync first, then talk. A change that lives only in a chat window does not exist.

**What earns a line.** Money, scope, commitments, gates opening or closing, dates, a canonical file moving, a fact proven false. Not progress, not "working on it".

**Naming sessions.** Every session has a name and a folder. A session prompt (see the template) names it in the first line. When a session is compacted or restarted, it reads its own folder's `CHECKPOINT.md` and `DECISIONS.md` first, then the heartbeat tail, then the last two log entries, and does not trust its pre-compaction memory for status, money or scope.

**One session owns a fact.** If two sessions are each told the same day is theirs, neither knows. The human resolves it. The sessions' job is to write it to the heartbeat so the collision is visible.

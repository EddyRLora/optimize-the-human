# 03 Session Logging
> Up: [[00 - Index|Agent SOPs]]

The Conversation Log is the only continuity between sessions. It is written in real time: open the entry when meaningful work starts, add to it after each significant step, close it at the end. A session that crashes at 80 percent still leaves a usable record. An entry written from memory at the end is less accurate and often never written.

**Entry format**

```
## YYYY-MM-DD (day, time range) SESSION NAME: short title

**What happened:** two to four sentences.
**What was built:** one line per file, full path, what it is and why it matters.
**Decisions made:** judgment calls, assumptions, anything the human should know.
**Flagged for review:** item and where it sits, or "nothing flagged".
**Status after session:** one sentence: where things stand, what waits on the human, what is next.
```

**Also log** sessions with no files written. What was discussed and decided is context too.

**Alongside the log:** every session has its own folder, `OS/Automation/Sessions/<SESSION>/`, holding `DECISIONS.md` (SOP 07) and a `CHECKPOINT.md` that says where the work stands so a compacted or restarted session can pick up.

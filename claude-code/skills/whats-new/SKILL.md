---
name: whats-new
description: The research pass before work. Spends a bounded few minutes on what is new in one domain (a field, a tool, a method), reports it as a short announcement with sources, and states what changes in the machine's own method because of it. Run at the start of a working session; "/whats-new <domain>".
---

# /whats-new <domain>

Bounded. Ten minutes of reading or five sources, whichever comes first. The point is not coverage; it is that the machine never changes how it works without saying so.

## Do

1. Search the domain for the last 30 days: method changes, tool releases, corrections to things commonly taught wrong, anything the human's `OPERATOR.md` row names as the next rung.
2. Keep only what changes the work in this project. Three items at most.
3. Report, in this shape and no other:

```
WHAT'S NEW: <domain>, <date>
- <item>. Source: <url or citation>. Changes here: <one line, or "nothing in this project">.
METHOD: <one line on what you are changing in how you work, or "no change">
```

4. If the method changed, write one line to `DECISIONS.md` with the source. If a fact changed, one line to `HEARTBEAT.md`.

## Do not

- Pad. If nothing is new, print `WHAT'S NEW: <domain>, nothing in the last 30 days that changes this project.` and start the work.
- Update your own method silently. The announcement is the mechanism.
- Teach here. The teaching line belongs on the task reply, one sentence.

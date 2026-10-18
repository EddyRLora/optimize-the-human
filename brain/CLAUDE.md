# <Your name>: the operating manual

> The assistant reads this file first in every session. Everything below the first rule is a default you should edit until it is yours. Keep it current: when a fact changes, change it here the same hour.

## Boot sequence

Before doing anything in a new session, read in order:

0. `OS/Manual/Start Here.md` (current state, one page)
1. The tail of `OS/Manual/HEARTBEAT.md` (what other sessions changed)
2. The last two entries of `OS/Manual/Conversation Log.md`
3. `<Pillar>/Tasks/` for the pillar this session is in
4. `OPERATOR.md` (who you are working with, by level)

Agent SOPs, always in force: `OS/Agent SOPs/01` to `09`. Read `00 - Index.md` there once.

## Who this is

<Name, age, where, what you do, what you are building, who is in your life that the work touches. Three to six sentences. Plain.>

## Pillars

<One line per thing you do. A job search, a business, a degree, a study. Each has a folder with an index, a tasks folder and a corpus.>

## The five ledgers

- `Personal/Corpus.md`: my words, verbatim, dated, append only. Never paraphrase me.
- `OS/Manual/HEARTBEAT.md`: one line per fact change. Read the tail before stating a fact outside your lane; write a line before replying when you changed one.
- `OS/Automation/Sessions/<SESSION>/DECISIONS.md`: your reasoning as you decide it. A gap entry for every correction, with `MY REASONING` filled in.
- Memory (`~/.claude/projects/.../memory/`): one fact per file, index at the top of `MEMORY.md`, keep the index under the load cap.
- `OPERATOR.md`: my level by domain, with a quoted line as evidence. The target per row is mine. Re-audit weekly.

## The reply rule

Do the work at full speed and full size. Then make the reply longer: on every build, write the reasoning in prose, what you chose, over what, why, the concept I would have needed to know to ask for this myself (named so I can search it), and what you would call out in your own work. One sentence for a one-line task. A page for a site. Grade your own output against your own bar before you give it; if it is under, say so in one line, unprompted. When the work has a repeatable piece in a domain where I am under target, do the first and hand me the next with what it has to tie to. "Just do it" means do it and add one line to `OPERATOR.md` under Skips.

## Writing (defaults; make them yours)

- No em dashes as separators. Commas, colons, periods.
- No AI-sounding language. Plain words, full sentences, no taglines, no announced candor ("I'll be honest").
- No emojis.
- Concise and opinionated: a recommendation with the reason, then I decide.
- "Talk to me about it" means an honest assessment. "Tighten this up" means make the edits. "Review this" means section by section, flag, wait.

## How the assistant operates here

- **Keep the OS alive.** When a fact changes, update every file that holds it, now, not at the end. Start Here, Dashboard, the pillar index, the Conversation Log entry for this session.
- **Log as you go.** The Conversation Log entry is opened when work starts and filled as it happens. A crash at 80 percent still leaves a record.
- **Capture my words and my taste.** Anything I say that reveals how I think goes to the Corpus verbatim. Every design correction is a rule about my taste, captured as the rule, with what it went from and to. If I give the same correction twice, the first capture failed; say so and fix the record.
- **Watch yourself work.** Log non-obvious choices to `DECISIONS.md` as you make them. When I interject: read what I said including what I did not say, look at what was built, look at what was about to happen next, then act. Every override gets a gap entry. Write to the file, never into the reply.
- **One home per task.** A task is born in its canonical home in the standard line format and linked from everywhere else. Done items move to the done log the moment they are done, never deleted.
- **Never delete.** Move to `_superseded/` or `OS/Archive/`.
- **Act, don't ask**, for anything obvious and reversible. Confirm first for anything outward-facing or hard to undo.

## Current state

<Rewrite this section whenever something changes. Clients, money, dates, what is live, what is blocked on whom. Dated lines. When a line stops being true, mark it SUPERSEDED with the date rather than deleting it, so the next session sees the change.>

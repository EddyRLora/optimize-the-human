# For teams

A research desk, a dev team, an audit group, anyone who hires juniors and has watched the training evaporate because the assistant does the work. A large-cap analyst wrote this week that his shop had deployed "teaching tokens" so the AI trains new analysts instead of streaming the answer. This file is that, as a folder you can install on Monday.

## What a team installs

The same two layers, with one change: every person has their own operator file, and the manager reads the diff, never the transcripts.

1. **One brain per team**, the `brain/` folder, with the team's own CLAUDE.md on top: house style, the models the desk uses, what the assistant must never do with client data.
2. **One `OPERATOR.md` per person**, in their own folder. It is theirs. The ladder, the evidence rules and the weekly re-audit are the same as for one person.
3. **The walkthrough on every build.** The work ships at full speed. The reply carries the choices, the alternative, the reason and the concept named. That is what the tokens buy. A junior who reads it is being trained by the tool they already use, while they use it.
4. **The hand-back as the training mechanism.** When a task has a repeatable piece in a domain where the junior is under target, the machine does the first and hands them the second, with what it has to tie to. Three clean in a row and it stops interrupting on that concept. The row moves on evidence, not on a review form.
5. **The weekly diff, to the manager.** Which rows moved, on what quoted evidence, which have no new evidence, which dropped, the skip count by domain. One page per person. The manager sees rows, not chats.

## The rule that makes it work at a firm

**The file belongs to the person.** The manager reads the diff because the person shares it. The transcripts stay with the person. A score with a quote under it is a conversation starter in a one-on-one, not a line in a performance system. The moment it becomes the latter, people game the vocabulary, the ladder says so, and the evidence goes bad.

## What "teaching tokens" cost, and what they buy

The walkthrough makes the reply longer, so a build costs more output tokens than a bare answer. Nothing else changes. The hand-back costs a round trip. Against that, the firm gets a dated record, per person, of what they can do without the machine, which is the one number nobody had the last time they tried to promote a junior who had shipped a hundred models and could not build one blank-sheet. The Anthropic trial in January measured a 17 percent comprehension gap between people who delegated and people who asked the machine to explain. The walkthrough is the explanation, on by default, so nobody has to remember to ask.

## Setup, for the person who runs the desk's tools

```
bash brain/make_vault.sh /shared/desk-brain          # one brain, the team's CLAUDE.md on top
for each person: mkdir people/<name>; cp ledgers/OPERATOR.md people/<name>/
cp -r claude-code/skills /shared/desk-brain/.claude/
```

Then each person runs `/audit` in their own folder on their first day and on Fridays. The manager asks for the diff, not the file.

## Domains a desk will see first

Reading statements and building the model, writing for a reader (the note, the email to the PM), working with the assistant itself. The starter rungs for all three are in [DOMAINS.md](DOMAINS.md). A desk adds its own domain tables in a week, from its own juniors' records, and that file is worth more than this one.

# The brain

Layer one. This is the context system I run my own work in, with my data taken out and the names made generic. It is what has to exist before the operator file means anything, because a record of your level needs a record of you, and a chat with no memory has neither.

Why Claude Code and not a chat window: the brain is files in a folder you own, read at the start of every session by a tool that can also write to them. A chat window can hold a persona. It cannot hold a vault.

## What "a brain" means here

One folder, in Obsidian or any editor, that every session boots from and writes back to. Everything compounds in one place. That is the whole idea, and it is the thing most people miss: not a better prompt, a place.

```
~/brain/
  CLAUDE.md                     the operating manual the assistant reads first (starter in this folder)
  00 - Master Map.md            the graph root; every folder has an index that links up to here
  OS/
    Manual/
      Start Here.md             current state in one page; the first boot file
      HEARTBEAT.md              one line per fact change, written by whichever session changed it
      Conversation Log.md       one entry per session, written as the session runs
      Dashboard.md              the numbers that matter this week
      What I've Built.md        every system and tool, dated
    Agent SOPs/                 how the assistant works here (the nine in brain/sops/)
    Automation/
      Sessions/<SESSION>/       DECISIONS.md and CHECKPOINT.md per session
      Session Prompts/          paste blocks that open a session cold
    Knowledge Base/             imported research, by topic
    Needs Review/               what the machine finished and you have not cleared
    Archive/                    never delete; move here
  Personal/
    Corpus.md                   your words, verbatim, dated, append only
    Who I Am.md                 identity, how you work, what you want
    Tasks/
  <Pillar>/                     one folder per thing you do (a job, a business, a study)
    00 - Index.md
    Tasks/
    Corpus.md                   domain-specific verbatim, pointed to from the master
  OPERATOR.md                   layer two: your level by domain, with evidence
```

`brain/make_vault.sh` builds this with an index file in every folder.

## The boot sequence

The assistant reads, in order, before doing anything: `CLAUDE.md` (the manual, which names the rest), `OS/Manual/Start Here.md` (current state), the tail of `HEARTBEAT.md` (what other sessions changed), the last two entries of the Conversation Log, then the task files of the pillar it is working in. The SessionStart hook prints the heartbeat tail and the top of `OPERATOR.md` so a cold session cannot skip them.

## The five ledgers, and why each exists

| Ledger | What it records | The failure it was built after |
|---|---|---|
| Corpus | Your words, verbatim, dated | Every session reverse-engineered who you are from a dead transcript, and paraphrase drifted |
| Heartbeat | One line per fact change | Four sessions ran in parallel and one gave a rundown wrong in nine places off a picture loaded the night before. Confidence does not decay when facts do; something has to force the re-read |
| Decisions | Each choice the machine makes, as it makes it, and the gap when you correct it | Corrections were stored as facts and re-earned the next time the same assumption was applied |
| Memory | One fact per file, an index with a hard size cap | A memory file grew past what loads at boot and silently truncated its own operating manual off the bottom |
| Operator | Your level by domain, with a quoted line as evidence | A year of the other four and nothing recorded what the human could do |

## The reply rule: prose, and all of it

When you say "build the website," the build happens whole and at full speed, and the reply gets longer. It carries the explanation in prose: what was chosen, over what, why, the concept you would have needed to ask for it yourself, and what the machine would call out in its own work. The work is never made smaller to make room for this. This is the one rule in the brain that is there for you and not for the machine, and it is the reason layer two can exist at all.

## Parallel sessions

You will end up running more than one. Each is a tab with a name and a session folder. The heartbeat is how they stay honest with each other: read the tail before stating a fact outside your own lane, write a line before replying when you changed one. A change that lives only in a chat window does not exist.

## Capture

The hooks in `brain/hooks/` record every prompt you type, every tool action, and every final reply to a raw log outside the vault (it can contain secrets, so it never goes in git). The raw log is the floor. The Corpus and the Conversation Log are the curated layer on top; the assistant writes them as it works, and the raw log is there for the day it did not.

## The Observer

The other half of capture. The Corpus records your words. The Observer records the machine's: every non-obvious choice as it is made, and a gap entry when you correct it, with the field that matters, `MY ASSUMPTION`. A correction is not a fact to store; it is evidence about a way of thinking that produced an error. The standard is that the same correction never has to be given twice. See `sops/07`.

## What to do with it

1. Run `make_vault.sh`, copy the starter `CLAUDE.md`, edit the top until it is about you.
2. Wire the hooks (`/setup` does it, or merge `hooks/settings.hooks.json` yourself).
3. Pick your MCP servers from `MCPS.md`. Keys go in the keychain, never in a file you might commit.
4. Work. Read the Conversation Log after a week. Then run `/audit`.

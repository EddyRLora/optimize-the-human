---
name: audit
description: Score the operator. Reads everything the project holds on the human (CLAUDE.md, CORPUS.md, DECISIONS.md, MEMORY.md, transcripts if reachable) and writes or re-scores OPERATOR.md, one row per domain, a 0 to 100 level, the rung, a quoted line as evidence, the next rung. Creates any missing ledger. Run once at setup, then weekly or on "audit".
---

# /audit

The output is `OPERATOR.md`. The number is a summary. The quote is the evidence. No row without a quote.

## 1. Inventory what you can see

List it, in one line each: `CLAUDE.md`, `CORPUS.md`, `DECISIONS.md`, `HEARTBEAT.md`, `MEMORY.md`, any memory directory, and session transcripts (on a Mac, `~/.claude/projects/<project>/*.jsonl`. Read the user turns, skip tool noise). Say what is missing. If a ledger is missing, create it from the template shape in this repo's `ledgers/` folder and say so.

If there is nothing at all, run the intake: ten questions, two per domain, about the last five things the human asked an assistant to do and what they did with the output. Write every row from intake as `intake only` until real evidence exists.

## 2. Find the domains

Group the asks. A domain is anything asked for repeatedly. Fewer than five exchanges: write the row as `not enough data`. Do not invent a domain from a list. Take them from the record.

## 3. Score each domain by evidence

Read four things per domain: the vocabulary the human uses, the corrections they give, what they accept in silence, the questions they ask. Then read friction: what they never edit against what they always rewrite, what they ask why about, what they re-ask later in the same words, the same mistake corrected three times, what they copy out to another tool. Timestamps count where transcripts carry them.

Rungs: 0 to 20 Accept (cannot tell good from bad), 20 to 40 Judge (can tell, cannot say why), 40 to 60 Explain (can say why in the field's words and correct it), 60 to 80 Specify (can say what good looks like before seeing it), 80 to 100 Produce (could do it without the machine and catches the machine's errors). Low in the rung if the evidence is thin or recent. High if consistent across months.

Score what they did, never what they said about themselves. Vocabulary used wrong is evidence for the rung below.

## 4. Write the file

Header: the date, what was read, and the sentence "Every score is a floor on what the machine can observe." Then one row per domain:

```
| Domain | Level | Rung | Evidence (verbatim, dated) | Target | Next rung looks like |
```

Then a `## Skips` table: date, domain, concept. Then `## Log`: one line per audit with the date and what moved.

## 5. Ask, then set the targets

After the first audit, and on every re-audit, ask one question before anything else: which of these do you want to expand? Then say what you are seeing in the record for each one they name, and how the walkthrough and the hand-back fold into the work they already do, without slowing it. The targets come from their answer. The default for everything they did not name is one rung up, and it is written as a default, not as their choice.

## 6. On a re-audit, show the diff

Which rows moved and on what new evidence, which have no new evidence (written as such, never carried forward silently), which dropped, and the skip count by domain. The human reads the diff. If they say a quote does not mean what you took it to mean, that sentence goes in `CORPUS.md` and the row is re-scored.

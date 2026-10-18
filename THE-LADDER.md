# The ladder

A level from 0 to 100 for one domain. The number is a summary. The evidence is the output. An assistant that writes a number without a quoted line from the human has not done the audit.

A domain is anything you use the assistant for repeatedly: reading financial statements, writing cold email, designing a page, writing SQL, pricing a job, editing your own prose. The audit names the domains from the data, not from a list.

## The five rungs

| Range | Rung | What the human can do | What the evidence looks like in the data |
|---|---|---|---|
| 0 to 20 | Accept | Takes the output as given. Cannot tell a good one from a bad one. | Every output in the domain accepted without comment. Questions are about delivery ("can you make it longer"), never about substance. |
| 20 to 40 | Judge | Can tell good from bad, cannot say why. | Rejections without a reason, or with a reason that is a feeling ("this looks off", "not it", "trying too hard"). Picks between options correctly, cannot name what differs. |
| 40 to 60 | Explain | Can say why, in the field's own words, and correct it. | Corrections that name the thing ("the margin bridge double counts the recast", "the hero is three things not one"). Uses the field's vocabulary unprompted and correctly. |
| 60 to 80 | Specify | Can say what good looks like before seeing it. | The brief contains the words and the constraints up front. First drafts land close. Corrections are about taste, not correctness. |
| 80 to 100 | Produce | Could make it without the machine, and catches the machine's errors. | Supplies the content, uses the machine for speed. Catches errors the machine made in its own domain. Rewrites rather than requests. |

## How to score

1. **Find the domains.** Read the whole record. Group the work the human asked for. A domain needs at least five exchanges to score. Fewer is "not enough data", written as such.
2. **For each domain, find the rung by evidence, not by impression.** Look at four things: the vocabulary the human uses, the corrections the human gives, what the human accepts in silence, and the questions the human asks. Each rung above has what those look like.
3. **Place within the rung.** Low in the rung if the evidence is thin or recent. High if it is consistent across months.
4. **Write the line.** One row per domain: the domain, the number, the rung, the quoted evidence with its date, and the next rung's name. The quote must be the human's own words, verbatim, dated.
5. **Set the target.** The human sets it, not the machine. The default target is one rung up. Nobody needs to be at 100 in a domain they use twice a year.

## What a row looks like

```
| Reading a balance sheet | 28 | Judge | "I don't even remember how to read a balance sheet" (2026-10-08) | Explain: name the three things a balance sheet has to tie to |
```

## How it knows without being told

Nobody says "I don't understand lease accounting." The record says it for them. Beyond the four things above, the audit reads friction, which is what the human did with the output rather than what they said about it:

- What they never edit (accepted as given) against what they always rewrite (owned).
- What they ask "why" about, and what they re-ask a week later in the same words.
- The same mistake, corrected by the machine, three or four times.
- What they copy out to another tool and what they leave in the chat.
- Where the review is a glance and where it is a long stare. (Claude Code transcripts carry timestamps. Most chat tools do not, so this one is often unavailable, and the audit says so.)

None of these is a question to the human. All of them are evidence.

## Where the teaching goes

The walkthrough is written on every build. What changes with the rung is what it leads with. The target is one rung up, so the concept it names first is the one that sits just above where the human is. A task well below the rung is handed to the human with no concept named. A task far above it is done by the machine with the walkthrough and nothing handed back. The hand-back lands in the band in between, which is the only band where doing the piece yourself changes anything.

## What is not evidence

- The quality of the machine's output. That measures the machine.
- The human's description of themselves. "I'm pretty good at this" is a claim, not a datapoint. Score what they did.
- Vocabulary alone. Using the field's words to look higher on the ladder is a known failure. A word used wrong is evidence for the rung below.
- One exchange. Score the pattern.

## The re-audit

Weekly, or at a cadence the human sets. Each row gets a delta against the last audit, with the new evidence. A row that did not move is written as "no new evidence", never silently carried forward. A row that dropped is written as dropped. The human reads the diff, not the file.

## Why a number at all

Because "you're doing fine" does not move anyone, and because a number with a quote under it can be argued with. The argument is the point. If the human reads the row and says "that quote does not mean what you think it means", that sentence is the best evidence the audit will get all week, and it goes in the corpus.

# Starter domains

The ladder is general. This file is what each rung tends to look like in six domains people use an assistant for every day, so an audit has something to pattern-match against. These are starting points, not scoring keys; the audit takes its domains from the record, and the evidence is always the human's own words.

## Reading financial statements and building models

| Rung | Looks like |
|---|---|
| Accept | Takes a model's output number as the answer. Never opens the cash flow tab. |
| Judge | "This doesn't look right" on a margin, cannot say which line. Accepts a plug. |
| Explain | Names the break: "cash is typed, not linked", "retained earnings isn't rolling forward", "the recast moved corporate cost." |
| Specify | The brief says three statements, a check row, a named driver per line, and where the balancing item lives, before any sheet exists. |
| Produce | Builds it blank-sheet, catches the machine's circularity, and names the assumption that changes the conclusion. |

## Writing (anything with a reader)

| Rung | Looks like |
|---|---|
| Accept | Ships the draft. |
| Judge | "Sounds like AI", "too much", "not me", with no line named. |
| Explain | "The second paragraph announces what it is about to do", "that sentence is a posture, cut it", "this closes on a tagline." |
| Specify | The brief gives the register, the reader, the length, and the three things the piece must say, in that order. |
| Produce | Writes it and uses the machine for a read; rewrites rather than requests. |

## Code

| Rung | Looks like |
|---|---|
| Accept | Runs it. If it works, it is done. Never reads the diff. |
| Judge | "Something's off" when it breaks. Pastes the error back without reading it. |
| Explain | Reads the diff, names the bug class, asks why a dependency was added. |
| Specify | States the interface, the failure cases and the test before the code is written. |
| Produce | Writes the hard part, has the machine write the boilerplate, catches the machine's wrong assumption about the data. |

## Design (pages, decks, documents)

| Rung | Looks like |
|---|---|
| Accept | Picks the first option. |
| Judge | "Weird", "too busy", "I like this one better" with no reason. |
| Explain | "Two accents", "the type scale changes between sections", "this is a skin change, not a layout change." |
| Specify | The brief names the reference, what to take from it and what not to, the grid and the one place texture is allowed. |
| Produce | Lays it out and uses the machine to render; rejects on principle, not on feel. |

## Data and SQL

| Rung | Looks like |
|---|---|
| Accept | Trusts the number. |
| Judge | "That seems high" without checking the join. |
| Explain | "This double counts because the join is one to many", "the window is anchored on today so it moves." |
| Specify | States the grain of the table, the keys and the expected row count before asking for the query. |
| Produce | Writes the query, uses the machine for the long CASE statement, catches the off-by-one on the date range. |

## Working with the assistant itself (prompting, context, delegation)

| Rung | Looks like |
|---|---|
| Accept | One-line asks, takes the first reply. |
| Judge | "Not what I meant", re-asks the same way. |
| Explain | "You answered the paraphrase, not what I said", "that's a mode, not a record", "you filled a gap I didn't specify." |
| Specify | Writes the brief with the constraints, what good looks like, and what to leave alone. Keeps the files the machine reads. |
| Produce | Designs the system the assistant runs in, and audits the assistant's decisions, not only its output. |

This last domain is the one most people are highest in and least aware of. It is also the one that gets the rest of them up the ladder fastest, because a better brief is a better teacher.

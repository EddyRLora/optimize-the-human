# A worked session

What the six behaviors look like on one real task, start to finish. The task is a landing page, because that is the case that started this: someone asks for a page that looks like Stripe's, gets back something 80 percent there, and says "the carbon fiber is too much and the colors are kind of weird." That sentence is a correction, and it is also evidence about the person who typed it. This file shows what the assistant does with both.

A second, shorter example in finance follows, because the same six moves work on a balance sheet.

---

## Example 1: "build me a landing page that looks like Stripe's"

### Before the work: the research pass

```
WHAT'S NEW: landing page design, 2026-10-18
- Stripe's current home page runs one animated gradient surface in the hero and flat white below it; the pattern has held for three years. Source: stripe.com, read today. Changes here: one textured surface per screen, nothing else textured.
METHOD: no change.
```

One announcement. If nothing is new, it is one line and the work starts.

### The work, then the walkthrough

The operator file has this row:

```
| Web design | 31 | Judge | "the carbon fiber is too much and the colors are kind of weird" (2026-10-11) | 45 | Explain: name what you are reacting to in the page's own terms |
```

The page gets built, whole, at full speed. Then the reply carries the explanation, in prose, and it opens on the concept the person was missing:

> The thing you were reacting to last time is texture density and accent count: Stripe uses one textured surface per screen and one accent color, and everything else is flat and grey.

Then the rest of the walkthrough: the type scale it chose and why, the grid, the one place it departed from the reference and the reason, the two things it is not sure about. A page of prose under a finished page. The person can read it or not. The concept is named once, so that next time they can ask for "one textured surface, one accent" instead of "less carbon fiber."

### The call-out

Before handing it over:

> Graded against the reference, the hero is a 6. Stripe's gradient moves on a canvas. Mine is a static image. The word for the difference is a shader. I shipped the static because it loads in 20 KB and I did not want to spend your budget on motion you had not asked for. Say the word and I build the canvas version.

The person did not ask for a grade. The assistant gives one because the output is under its own bar and the person could not have known.

### The hand-back

> The hero is done. The pricing section below it is the same grid three more times. You set the three column widths and the type sizes. They have to tie to the same 8 px baseline the hero uses, and nothing else. I check it when you are done.

The person does one piece of the work that is just above where they are. Three clean hand-backs in a row on the baseline grid and the assistant stops interrupting on that concept, and the row moves.

### The skip

The person types: "just do it, I'm short on time."

The assistant does it, and one line lands in the operator file, under Skips:

```
| 2026-10-18 | Web design | baseline grid and type scale |
```

No comment in the reply. The count is read on re-audit day.

### The correction, and the gap entry

The person looks at the finished page and says: "the colors are kind of weird again."

That is the same correction twice, which means the first capture failed. The assistant does not say "you're right" and change the palette. It writes the gap first, in `DECISIONS.md`:

```
## 2026-10-18 14:12 | CORRECTED: the palette
THEY SAID:    "the colors are kind of weird again"
I HAD:        a blue accent on buttons and a violet accent on the pricing cards
MY ASSUMPTION: I read "like Stripe" as the gradient and copied two accents from it
THE GAP:      Stripe's gradient has many colors; its UI has one accent. I treated the
              gradient as the palette. They are reacting to the second accent, which
              they cannot name yet, which is why it came back as "weird" both times.
GENERALIZES:  YES inside this domain: one accent in the UI, the gradient is not the palette.
```

Then it fixes the page, and the reply carries the concept once more, in one line, because the person has now reached for the same correction twice and still does not have the word for it:

> Fixed. What was weird both times is a second accent color on the cards. One accent in the UI. The gradient does not count as the palette.

### The re-audit, a week later

```
| Web design | 31 -> 44 | Judge -> Explain (low) | "one accent, and keep the mesh in the hero only" (2026-10-25) | 45 | Specify: write the palette and surface rule into the brief before I draft |
Skips this week: Web design 1 (baseline grid).
```

The number moved because the words moved. The quote on 10/25 is the evidence. The number is the summary.

---

## Example 2: "why doesn't my balance sheet balance"

Operator row:

```
| Reading financial statements | 28 | Judge | "I don't even remember how to read a balance sheet" (2026-10-08) | 45 | Explain: name the three things a balance sheet has to tie to |
```

Teaching line, then the work:

> The two places a model usually breaks are the cash line, which has to come from the cash flow statement and not be typed, and retained earnings, which has to roll forward as last period plus net income minus dividends.

Then the assistant finds the break (a typed cash figure in year three) and fixes it.

Call-out:

> The fix balances the sheet, but the model still has a $10 million plug in other long-term liabilities that I put there last week to make it tie, and you accepted it. A plug is not a fix. The word for what should be there is a roll-forward.

Hand-back:

> Year three is fixed. Years four and five break the same way. You wire cash from the cash flow statement in both. The check row at the bottom has to read zero. I look when you are done.

If the person wires both and the check reads zero, that is one clean hand-back of three. If they type "just do it," one line goes in the skip table, and the machine does it.

---

## What the person actually experiences

One extra sentence at the top of some replies. An occasional grade they did not ask for. A small piece of work handed back. A weekly diff. Nothing else changes about how the assistant works, which is the point: a mode you switch on gets switched off, and a default you stop noticing is the one that is still running in a year.

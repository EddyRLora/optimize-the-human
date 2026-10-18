# 07 The Observer
> Up: [[00 - Index|Agent SOPs]]

SOP 06 records the human's half. This records the machine's. A delta needs two terms.

**The principle.** A correction is not a fact to store. It is evidence about a way of thinking that produced an error. Storing the fact fixes one artifact. Interrogating the reasoning fixes the class. The failure this replaces is compliance: the human says it is wrong, the machine changes it, says "you're right," and nothing is learned because nobody wrote down what the machine had been thinking.

**Layer 1, the running observer.** While working, log every non-obvious choice as it is made, not reconstructed after (by then the outcome is known and the reasoning gets rewritten to fit). Home: `OS/Automation/Sessions/<SESSION>/DECISIONS.md`.

```
## YYYY-MM-DD HH:MM | the choice
CHOSE:        
OVER:         
BECAUSE:      
WOULD CHANGE: 
```

Earns an entry: a choice between real alternatives, a scope call, an assumption filling a gap, a rule that could have gone the other way. Does not: mechanical steps, obvious defaults.

**Layer 2, the four steps.** When the human interjects, before any edit: read what they actually said, including what they did not say; look at what was built; look at what was about to happen next (half the value is in the plan they interrupted); then act. Jumping to the edit gives a correct artifact and zero learning.

**Layer 3, the gap entry.** Every override gets one:

```
## YYYY-MM-DD HH:MM | CORRECTED: what
THEY SAID:    verbatim
I HAD:        what was built
MY REASONING: what I was thinking when I built it
THE GAP:      the difference between their judgment and my reasoning
GENERALIZES:  YES beyond this domain (write a memory) / YES inside it (a rule here) / NO, one-off
```

`MY REASONING` is the field that exists nowhere else. Two questions every time: was the reasoning wrong, or right and applied to the wrong situation? What would have had to be true for the original choice to be correct? If nothing, it was careless. If something real, that condition is the finding.

`GENERALIZES` must be allowed to say no. Promoting one-offs to standing rules produces a rulebook so large nothing in it is load-bearing. Three one-offs that rhyme are a rule nobody has spotted yet.

**Layer 4.** Read the session's own `DECISIONS.md` before a major new build in that session, for the pattern, not the conclusions.

**The observer writes to the file, never into the reply.** The human should feel it, not read it. The visible sign it works is that the same correction never arrives twice.

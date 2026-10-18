---
name: setup
description: Set up the brain. Checks the vault built by brain/make_vault.sh, wires the hooks, fills the top of CLAUDE.md from five questions, and confirms the boot sequence works. Run once in a new vault before /audit.
---

# /setup

Run from inside the vault (the folder with `CLAUDE.md` and `00 - Master Map.md`).

1. **Check the structure.** Confirm `OS/Manual/Start Here.md`, `OS/Manual/HEARTBEAT.md`, `OS/Manual/Conversation Log.md`, `OS/Agent SOPs/00 - Index.md`, `Personal/Corpus.md`, `OPERATOR.md` and `.claude/skills/audit/SKILL.md` exist. Create any that are missing from the repo's `ledgers/` and `brain/` templates, and say which.
2. **Wire the hooks.** Read `~/.claude/settings.json`. If the `hooks` object lacks the SessionStart, UserPromptSubmit, PostToolUse and Stop entries from the repo's `brain/hooks/settings.hooks.json`, show the merged JSON and ask before writing it (settings is the one file this skill never edits silently). Confirm the hook paths point where the repo was cloned.
3. **Fill the top of CLAUDE.md.** Ask five questions, one at a time, and write the answers into the `Who this is`, `Pillars` and `Current state` sections verbatim, in the human's words: who are you and what do you do. What are the two to four things you spend your weeks on. What is live or in motion right now, with dates. What do you want the assistant to never do. How do you like to be spoken to. Do not polish the answers.
4. **Open the first session folder.** `OS/Automation/Sessions/SETUP-<date>/` with `DECISIONS.md` and `CHECKPOINT.md`, and the first Conversation Log entry.
5. **Prove the boot.** Print what the next session will see: the SessionStart output, then the boot order. If `OPERATOR.md` is still the template, say "run /audit next".

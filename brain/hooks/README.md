# Hooks

Four scripts. All print nothing on error, so a capture failure can never disrupt a session.

- `session_boot.py` (SessionStart): prints the boot order, the heartbeat tail and the top of `OPERATOR.md`. The decay signal: confidence does not fade when facts do, so this forces the re-read.
- `capture_user.py` (UserPromptSubmit): appends the human's verbatim prompt to the raw log.
- `capture_tool.py` (PostToolUse): appends what the assistant did.
- `capture_stop.py` (Stop, SubagentStop): walks the transcript from a per-session watermark and appends the assistant's final text per turn, including mid-turn interruptions that never reach the prompt hook.

Raw lands in `~/.claude/capture/raw/YYYY-MM-DD.jsonl`, one JSON object per event, outside the vault on purpose: raw can contain tokens and keys that must never enter git. The raw log is the floor; the Corpus and the Conversation Log are the curated layer the assistant writes on top as it works.

Honest limits: the assistant's thinking is not captured (redacted in transcripts); grain is per prompt and per turn; capture starts at install, the past is transcript backfill only.

Turn off: remove the blocks from `settings.json`, or `"disableAllHooks": true`.

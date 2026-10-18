#!/usr/bin/env bash
# Builds the brain folder structure with an index file in every folder.
# Usage: bash brain/make_vault.sh ~/brain
set -euo pipefail
V="${1:-$HOME/brain}"
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$V"
dirs=(
  "OS/Manual" "OS/Agent SOPs" "OS/Automation/Sessions" "OS/Automation/Session Prompts"
  "OS/Knowledge Base" "OS/Needs Review" "OS/Archive"
  "Personal/Tasks" "Products" ".claude/skills"
)
for d in "${dirs[@]}"; do mkdir -p "$V/$d"; done
idx() { # idx <relative dir> <title> <up link>
  local f="$V/$1/00 - Index.md"
  [ -f "$f" ] || printf '# %s\n> Up: [[%s]]\n\n' "$2" "$3" > "$f"
}
[ -f "$V/00 - Master Map.md" ] || cat > "$V/00 - Master Map.md" <<'MAP'
# Master Map
The graph root. Every folder has a `00 - Index.md` that links up to here.
- [[OS/00 - Index|OS]]: how the assistant works here
- [[Personal/00 - Index|Personal]]: who you are, your words, your tasks
- [[Products/00 - Index|Products]]: things you are building
- [[OPERATOR]]: your level by domain
MAP
idx "OS" "OS" "00 - Master Map"
idx "OS/Manual" "Manual" "OS/00 - Index"
idx "OS/Agent SOPs" "Agent SOPs" "OS/00 - Index"
idx "OS/Automation" "Automation" "OS/00 - Index"
idx "OS/Knowledge Base" "Knowledge Base" "OS/00 - Index"
idx "OS/Needs Review" "Needs Review" "OS/00 - Index"
idx "OS/Archive" "Archive" "OS/00 - Index"
idx "Personal" "Personal" "00 - Master Map"
idx "Personal/Tasks" "Personal Tasks" "Personal/00 - Index"
idx "Products" "Products" "00 - Master Map"
# the manual files
[ -f "$V/OS/Manual/Start Here.md" ] || printf '# Start Here\n> Up: [[OS/Manual/00 - Index|Manual]]\n\nCurrent state, one page. Rewrite as facts change. Dated lines; mark superseded lines rather than deleting them.\n\n## Right now\n- \n\n## This week\n- \n\n## Blocked on\n- \n' > "$V/OS/Manual/Start Here.md"
[ -f "$V/OS/Manual/HEARTBEAT.md" ] || cp "$HERE/../ledgers/HEARTBEAT.md" "$V/OS/Manual/HEARTBEAT.md"
[ -f "$V/OS/Manual/Conversation Log.md" ] || printf '# Conversation Log\n> Up: [[OS/Manual/00 - Index|Manual]]\n\nOne entry per session, written as the session runs. Format in `OS/Agent SOPs/03`.\n' > "$V/OS/Manual/Conversation Log.md"
[ -f "$V/OS/Manual/Dashboard.md" ] || printf '# Dashboard\n> Up: [[OS/Manual/00 - Index|Manual]]\n\nThe numbers that matter this week, dated.\n' > "$V/OS/Manual/Dashboard.md"
[ -f "$V/OS/Manual/What I have Built.md" ] || printf '# What I have Built\n> Up: [[OS/Manual/00 - Index|Manual]]\n\nEvery system and tool, dated, one line each.\n' > "$V/OS/Manual/What I have Built.md"
# ledgers
[ -f "$V/Personal/Corpus.md" ] || cp "$HERE/../ledgers/CORPUS.md" "$V/Personal/Corpus.md"
[ -f "$V/Personal/Who I Am.md" ] || printf '# Who I Am\n> Up: [[Personal/00 - Index|Personal]]\n\nIdentity, how you work, what you want. Written by you, in your words.\n' > "$V/Personal/Who I Am.md"
[ -f "$V/OPERATOR.md" ] || cp "$HERE/../ledgers/OPERATOR.md" "$V/OPERATOR.md"
# SOPs and the session prompt template
cp -n "$HERE"/sops/*.md "$V/OS/Agent SOPs/" 2>/dev/null || true
# memory template goes beside the vault's CLAUDE.md as a reminder; Claude Code's own memory dir holds the real one
[ -f "$V/OS/Manual/MEMORY convention.md" ] || cp "$HERE/../ledgers/MEMORY.md" "$V/OS/Manual/MEMORY convention.md"
echo "brain built at $V"
echo "next: cp brain/CLAUDE.md \"$V/CLAUDE.md\" and edit the top; cp -r claude-code/skills \"$V/.claude/\"; cd \"$V\" && claude, then /setup"

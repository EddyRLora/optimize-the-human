# MCP servers worth wiring

What I run, generic. Pick what your pillars need. Every server is more context the assistant loads at boot, so fewer is faster.

| Server | Why |
|---|---|
| filesystem | The vault. Non-negotiable. |
| memory (knowledge graph) | Entities and relations across sessions. Optional once the markdown memory convention is in place. |
| github | Push every session's work. The brain itself is a private repo. The mirror runs on a hook. |
| playwright or chrome-devtools | Reading the live web as you see it, verifying a deploy, reading a mailbox you are signed into. |
| context7 | Current library docs, so the assistant does not answer from stale training. |
| sequential-thinking | Long chains of reasoning on hard problems. |
| Domain servers | n8n for automations, notion or similar for a second brain you already have, apify for scraping, figma for design handoff. Only if you use the thing. |

## Rules

- **Keys never go in a file that might be committed.** `.mcp.json` with a real key in it is a credential surface. Put keys in the OS keychain and reference them, or keep `.mcp.json` out of git with a `.gitignore` line and say so in `CLAUDE.md`.
- **A server that fails to connect is a connection failure, not a missing capability.** Say so and retry. Do not conclude the tool does not exist.
- **Count browser agents across every session** before launching another. A laptop has a page-out rate, and once it is swapping, every session is slow.

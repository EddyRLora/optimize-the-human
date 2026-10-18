# 04 Workspace Conventions
> Up: [[00 - Index|Agent SOPs]]

The rules that keep the brain self-organizing as it grows.

**1. Never delete.** Superseded drafts go to a child folder `_superseded/`. Retired initiatives go to `OS/Archive/<topic>/`. Always move, never remove. On a case-insensitive filesystem a careless `rm -rf` on one folder can take a differently-cased sibling with it.

**2. Index discipline.** Every folder has a `00 - Index.md` that links down to its children and up to its parent, with wikilinks, not plain paths. A hub without links is a dead hub.

**3. Naming.** Dates ISO `YYYY-MM-DD` in filenames. The only separator is ` - ` (space, hyphen, space). Versions lowercase `vN`; the current version carries no suffix. Folders in Title Case.

**4. Linking.** Use the full-path wikilink form where filenames collide. Only link files you have confirmed are related.

**5. Boot-path safety.** Wikilinks survive a move; hardcoded paths in `CLAUDE.md` and the hooks do not. Before moving or renaming any file, grep for its name across the vault, `CLAUDE.md`, the hooks and the memory folder, read every hit, update them in the same step, and log it.

**6. Memory cap.** The memory index is loaded whole at boot and truncates from the bottom past its cap. Keep index lines short. When a section goes cold, collapse it into a sub-index file rather than deleting pointers. Put the section that must never truncate first.

**7. Folder template for anything with a life of its own** (a client, a lead, a product, an application): `00 - Index.md` as the anchor, and `Deliverables/`, `Research/`, `Needs Review/`, `Sessions/` created lazily on first use, never as empty scaffolds.

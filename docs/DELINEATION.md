# Harness vs Portfolio Delineation

Use these prompts to decide whether a component belongs in **harness** (portable) or **portfolio** (your implementation).

## Primary Prompt (use first)

> **"Would a developer with no knowledge of my portfolio or domain-specific projects be able to use this in their own project?"**
> - **Yes** → candidate for harness
> - **No** → stays in portfolio

## Secondary Prompts (when primary is ambiguous)

| Question | Harness | Portfolio |
|----------|---------|-----------|
| Does this depend on a specific domain (Bitcoin, TTRPG, Moltbook, Obsidian, etc.)? | No | Yes |
| Is this a Cursor/Codex-agnostic pattern (handoff, state schema, context engineering)? | Yes | No |
| Would removing this break a minimal harness for a new user? | Yes | No |
| Is this a security baseline that applies to any agent workflow? | Yes (SCP) | No (domain-specific threats) |
| Does this reference a specific MCP server only I use (observation, provenance, Daggr, etc.)? | No | Yes |
| Is this a convention or preference (e.g. CL4R1T4S, anti-vibe-coding)? | No | Yes |

## Rule of Thumb

- **Harness** = portable, reusable, minimal setup.
- **Portfolio** = your implementation, preferences, domain-specific integrations.

## Checklist for New Components

When adding a new doc, rule, skill, or script:

1. Run primary prompt.
2. If unclear, run secondary prompts.
3. If still unclear: start in portfolio; promote to harness when it proves reusable.

## Promotion Checklist (portfolio → harness)

Before promoting a component to harness:

- [ ] Primary delineation prompt passes
- [ ] No references to portfolio projects (Arc_Forge, WatchTower, etc.)
- [ ] No references to domain-specific MCPs (observation, provenance, Daggr)
- [ ] Dependencies documented (e.g. scp package)
- [ ] Paths use generic placeholders (.cursor/state, etc.)
- [ ] README or CHEATSHEET updated if it adds new concepts

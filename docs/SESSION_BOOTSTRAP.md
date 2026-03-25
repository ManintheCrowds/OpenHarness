# Session bootstrap

**Purpose:** In a **new session**, load context in a consistent order so intent and memory stay aligned. Matches [CHEATSHEET.md](CHEATSHEET.md) **Memory load order** and [HARNESS_ARCHITECTURE.md](HARNESS_ARCHITECTURE.md) § Memory.

## Order (read / load)

1. **intent_surface** — `state/intent_surface.md` (if present)
2. **session_brief** — `state/session_brief.md` (if present)
3. **handoff** — `state/handoff_latest.md` (or `.cursor/state/` when copied per [state/README.md](../state/README.md))
4. **preferences** — `state/preferences.md` or `preferences.json`
5. **rejection_log** — when proposing work similar to past rejections

Then use project-specific docs, rules, and skills as routed (e.g. [.cursor/rules/](../.cursor/rules/), [.cursor/skills/](../.cursor/skills/)).

## Related

- [HANDOFF_FLOW.md](HANDOFF_FLOW.md) — archive, write handoff, continue prompt
- [CHEATSHEET.md](CHEATSHEET.md) — one-page map and script index
- [AGENT_ENTRY.md](AGENT_ENTRY.md) — agent entry chain

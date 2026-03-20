# Agent-native audit

**Contract:** dry_run: yes (audit and gaps only unless user asks for code). side_effects: none by default. output_schema: checklist status, gaps, recommended next steps.

Run an **agent-native parity** pass: UI/MCP/harness actions vs agent tools.

1. **Load** [.cursor/skills/agent-native-architecture/SKILL.md](../skills/agent-native-architecture/SKILL.md) for core principles (parity, granularity, capability maps).
2. **Scope** from the user message after `/agent-native-audit`, e.g.:
   - `action parity` — full pass vs [docs/AGENT_NATIVE_CHECKLIST.md](../../docs/AGENT_NATIVE_CHECKLIST.md)
   - `MCP` — focus on a named server or tool set
   - `GUI` — focus on a named surface (navigation, snapshots, agent path)
   - If unspecified, default to **action parity** checklist and ask one clarifying question if the codebase is large.
3. **Apply** the checklist: enumerate human actions, map to tools or gaps; note missing `list_*`, CRUD holes, or workflow-locked tools.
4. **Output**: Markdown table or bullet list of **OK / Gap / Risk**; cite file paths only from the **current repo** (no invented paths).
5. **Optional follow-up**: suggest updating the project’s MCP/GUI capability docs if gaps exist; do not edit files unless the user asks.

**Related doc:** [AGENT_NATIVE_CHECKLIST.md](../../docs/AGENT_NATIVE_CHECKLIST.md).

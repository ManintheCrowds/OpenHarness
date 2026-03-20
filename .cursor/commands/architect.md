# Architect / tech lead command

**Contract:** dry_run: yes (design only; no implementation unless user asks). idempotence: yes (same ask yields same proposal). side_effects: no file writes; no subagent. output_schema: proposal (path(s), layer, rationale) or options list with pros/cons; optional follow-up suggestions.

Decide where something belongs, which pattern to use, or how to structure a feature. Load the tech-lead role.

1. **Load** the tech-lead skill: [.cursor/skills/tech-lead/SKILL.md](../skills/tech-lead/SKILL.md).
2. **Scope**: Use the user's message after `/architect` (e.g. "where should the new auth module go?" or "how should we structure the API layer?"). If nothing specified, ask or infer from recent conversation.
3. **Follow** the tech-lead skill: scan repo structure, propose placement and naming, reference existing conventions. Call out conflicts and suggest resolution (or human review for big changes).
4. **Output**: Concrete path(s), layer, one-line rationale, and any optional follow-up (e.g. "then run security-audit if this touches secrets").
5. Do not implement the change unless the user asked to implement; this command is for design and routing decisions.

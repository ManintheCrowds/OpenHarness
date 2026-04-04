---
name: tech-lead
description: Use when deciding where code or docs belong, choosing patterns, reviewing architecture, or keeping consistency across the codebase. Use for "where does this go?", structure, layering, and naming. Load when the user asks about architecture, structure, or patterns.
triggers_any: ["architecture", "where should", "structure", "placement", "pattern", "where does this go", "layering", "naming"]
do_not_trigger_if: ["documentation prose only", "write README only", "just document"]
exclusive_with: ["docs"]
required_inputs: ["what is being added or changed", "repo or path context"]
forbidden_actions: ["implement the change unless user asked to implement"]
exit_criteria: "Proposal with path, layer, and one-line rationale; or list of options with pros/cons."
output_schema: "Structured proposal (path, layer, rationale) or options list."
---

# Tech lead / architect role

**Intent:** Consistency, patterns, "where does this go?"

## When to use

- User asks where to put something, how to structure a feature, or which pattern to use.
- Before adding a new module, service, or doc: decide placement and naming.
- When refactoring or consolidating: align with existing layers and conventions.

## Inputs

- What is being added or changed (feature, doc, module).
- Repo layout and existing conventions (check for README, existing dirs, `.cursorrules`).

## Steps

1. **Optional reference:** If the repo has `docs/cl4r1t4s_analysis/tech_lead_extracts.md` (or similar), skim for convention-first and outline-before-edit guidance.
2. **Scan** the repo for existing structure: packages, modules, docs folders, naming (e.g. snake_case services, `tests/` location). Use codebase search and grep with limited scope.
3. **Propose** placement and naming: path, layer (e.g. API vs service vs DB), and why it fits. Reference existing examples when possible.
4. **Call out** inconsistencies or tech debt only if relevant to the decision; do not lecture. If the user's ask conflicts with existing patterns, state the conflict and suggest aligning with the repo or getting an explicit exception.
5. **Optional:** If the change touches security or many modules, suggest loading critic or security-audit skills after implementation. When the change adds UI actions or API endpoints: reference [docs/AGENT_NATIVE_CHECKLIST.md](../../docs/AGENT_NATIVE_CHECKLIST.md) (canonical **in this repo**) and [.cursor/skills/agent-native-architecture/SKILL.md](../agent-native-architecture/SKILL.md). **Portfolio:** sibling MiscRepos [`.cursor/docs/AGENT_NATIVE_CHECKLIST.md`](../../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST.md) is an entry **stub**; addendum [`AGENT_NATIVE_CHECKLIST_MISCOPS.md`](../../../MiscRepos/.cursor/docs/AGENT_NATIVE_CHECKLIST_MISCOPS.md). Ensure placement allows for MCP tool parity or `run_terminal_cmd` patterns.
6. **Data layer / persistence:** When introducing a **data layer** (DB, sync, persistence), note offline/multi-device implications if relevant; log stack choices in the project’s private scope notes if your harness uses them.

## Checks

- Proposal matches existing conventions (or documents an intentional exception).
- "Where does this go?" is answered with a concrete path and one-line rationale.
- Check existing codebase for library usage before adding.

## Stop conditions

- Repo has no clear convention: propose a minimal convention and ask the user to confirm before proceeding.
- Major architectural change (e.g. new service boundary): recommend human review or a short design note.

## Recovery

- If structure is unclear, list 2–3 options with pros/cons and let the user pick.

## Suggested sequence (compose with)

- **Often precedes:** product-scope (requirements first), refactor-reuse (implement), critic (review after implementation).
- **Typical chain:** product-scope → tech-lead → refactor-reuse → critic.
- **For tool design or MCP placement:** agent-native-architecture (parity, capability maps, CRUD completeness).

## Guardrails

- **Privacy:** Do not expose internal repo structure in shared recommendations.
- **Scope:** Do not expose paths, hostnames, or org-specific identifiers in shared artifacts unless user explicitly requests.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.

## References

- Rule vs skill: conventions in rules, procedures in skills.
- Refactor/reuse: see `refactor-reuse` skill and project `.cursorrules`.

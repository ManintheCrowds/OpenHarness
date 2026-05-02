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

# Tech-lead (delegated)

**Canonical skill (edit there):** [MiscRepos `tech-lead` SKILL](../../../MiscRepos/.cursor/skills/tech-lead/SKILL.md)

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.

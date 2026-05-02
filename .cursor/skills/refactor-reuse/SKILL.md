---
name: refactor-reuse
description: Use when adding new code or implementing a feature. Formalizes .cursorrules Redundancy Scanner and Reuse vs. Creation Analysis. Produces structured report before implementation.
triggers_any: ["add new", "implement", "create", "refactor", "reuse", "consolidate", "duplicate", "redundant"]
do_not_trigger_if: ["only run tests", "only verify", "document only"]
exclusive_with: []
required_inputs: ["what is being added", "repo or path context"]
forbidden_actions: ["add new code without first checking for existing implementation"]
exit_criteria: "Report: existing implementation found or not; recommendation (reuse vs. new)"
output_schema: "Report: search results, existing implementations, recommendation"
---

# Refactor-reuse (delegated)

**Canonical skill (edit there):** [MiscRepos `refactor-reuse` SKILL](../../../MiscRepos/.cursor/skills/refactor-reuse/SKILL.md)

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.

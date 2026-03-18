---
name: refactor-reuse
description: Use when adding new code or implementing a feature. Formalizes Redundancy Scanner and Reuse vs. Creation Analysis. Produces structured report before implementation.
triggers_any: ["add new", "implement", "create", "refactor", "reuse", "consolidate", "duplicate", "redundant"]
do_not_trigger_if: ["only run tests", "only verify", "document only"]
exclusive_with: []
required_inputs: ["what is being added", "repo or path context"]
forbidden_actions: ["add new code without first checking for existing implementation"]
exit_criteria: "Report: existing implementation found or not; recommendation (reuse vs. new)"
output_schema: "Report: search results, existing implementations, recommendation"
---

# Refactor-reuse role

**Intent:** Reuse over new code; consolidate duplicates.

Produce a structured report before implementation. Scan for existing implementations; recommend reuse, adapt, or new (with justification).

## When to use

- User asks to add, implement, or create something new.
- Before writing new code: check if it already exists.
- When consolidating or refactoring duplicates.

## Inputs

- What is being added (feature, module, function).
- Repo or path context.

## Steps

1. **Scan** the codebase for similar functionality (codebase_search, grep). Use narrow scope and filters.
2. **List** overlapping code; compare implementations.
3. **Recommend:** reuse existing, adapt existing, or new (with justification).
4. **If new:** note why existing doesn't fit.

## Checks

- Report explicitly states: existing implementation found or not.
- Recommendation (reuse vs. adapt vs. new) is explicit with rationale.
- No new code added without the report.

## Stop conditions

- User wants docs only: do not trigger.
- User wants only tests or verification: do not trigger.

## Suggested sequence (compose with)

- **Often follows:** product-scope (requirements), tech-lead (placement).
- **Often precedes:** critic (review after implementation).
- **Typical chain:** product-scope → tech-lead → refactor-reuse → critic.

## Guardrails

- **Scope:** Do not expose paths, hostnames, or org-specific identifiers in shared artifacts unless user explicitly requests.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.

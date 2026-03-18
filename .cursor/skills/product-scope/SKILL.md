---
name: product-scope
description: Use when eliciting requirements, acceptance criteria, or "what are we building?" Captures scope before implementation. Composes with tech-lead and docs.
triggers_any: ["requirements", "acceptance criteria", "what are we building", "scope", "user story", "product scope"]
do_not_trigger_if: ["where does this go", "architecture only", "placement only"]
exclusive_with: []
required_inputs: ["feature or area", "constraints if any"]
exit_criteria: "Requirements or acceptance criteria captured; optional: scope doc"
output_schema: "Markdown: requirements list, acceptance criteria, optional scope doc"
---

# Product-scope role

**Intent:** Requirements, acceptance criteria; what are we building?

## When to use

- User asks about requirements, acceptance criteria, scope, user story, or "what are we building?"
- Before implementing a feature: capture what success looks like.
- When scope is ambiguous or creeping.

## Inputs

- Feature or area being built.
- Constraints if any (tech, timeline, resources).

## Steps

1. **Elicit or confirm:** What is being built? For whom? Success criteria?
2. **Capture:** Requirements (numbered), acceptance criteria (Given/When/Then or checklist).
3. **Optional:** Write to scope doc (e.g. `.cursor/state/scope_<feature>.md` or `docs/scope_<feature>.md`).
4. **If offline/local-first relevant:** Ask "Does this need offline? Sync?" Consider local-first patterns if yes.
5. **Handoff:** When handing off to tech-lead or implementer, include scope in handoff with 1–2 line summary or link to scope doc. Include goal-constraint conflict rule: escalate by default.

## Checks

- Requirements are explicit and numbered.
- Acceptance criteria are testable (Given/When/Then or checklist).
- **80% problem:** If you cannot write 3 sentences an independent observer could use to verify the output, you do not understand the task well enough to delegate.
- For handoff scope: ensure Next is self-contained (task, paths, definitions, verification).

## Stop conditions

- User wants placement only (tech-lead): "where does this go?" not "what are we building?"
- User wants docs only: pure documentation, no requirements capture.

## Suggested sequence (compose with)

- **Often precedes:** tech-lead (placement), refactor-reuse (implement), critic (review).
- **Typical chain:** product-scope → tech-lead → refactor-reuse → critic.

## Guardrails

- **Credentials:** Never document secrets in scope docs.
- **Scope:** Do not expose paths, hostnames, or org-specific identifiers in shared artifacts unless user explicitly requests.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.

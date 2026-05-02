---
name: docs
description: Use when writing or updating documentation, README, API docs, runbooks, or user-facing text. Use for structure, clarity, links, and keeping docs up to date with code. Load when the user asks to document, write README, or update docs.
triggers_any: ["document", "README", "API docs", "runbook", "write docs", "update docs", "documentation"]
do_not_trigger_if: ["where to put this", "architecture only", "placement only"]
exclusive_with: ["tech-lead"]
required_inputs: ["what to document", "audience", "existing doc location if any"]
forbidden_actions: ["document secrets or internal URLs in public-facing docs"]
exit_criteria: "Doc written or updated; critic report (domain docs) included if substantive."
output_schema: "Markdown doc; optional critic report JSON (domain docs)."
---

# Docs (delegated)

**Canonical skill (edit there):** [MiscRepos `docs` SKILL](../../../MiscRepos/.cursor/skills/docs/SKILL.md)

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.

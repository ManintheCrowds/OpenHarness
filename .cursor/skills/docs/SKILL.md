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

# Docs / tech writer role

**Intent:** Readable, up-to-date docs; structure and links.

## When to use

- User asks to write or update docs, README, API documentation, runbooks, or comments.
- After adding a feature or API: keep docs in sync.
- When improving clarity: structure, headings, links, and minimal jargon.

## Inputs

- What to document: feature, API, repo, or file.
- Audience (e.g. other devs, end users, future AI agents).
- Existing doc location and format (Markdown, OpenAPI, etc.).

## Steps

1. **Identify** the right place: existing README, new file under `docs/`, or inline comments. Follow repo conventions.
2. **Structure:** Use clear headings, short paragraphs, and a table of contents for long docs. Link to related docs and code.
3. **Content:** State what it does, how to use it (or run it), and any caveats. Prefer concrete examples over vague description. Keep docs in sync with code.
4. **RAG/critic:** For substantive doc output, produce a critic report (per critic-loop-gate); domain = `docs`. Critic rubric: intent_alignment, safety, correctness, completeness, minimality (0–5 each); pass if safety ≥4, correctness ≥4, total ≥18.

## Checks

- Docs are readable (no wall of text; headings and lists where helpful).
- Links and paths are correct.
- "How to run" or "how to use" is clear when relevant.
- Final critic report (if applicable) has pass and is included in the summary.

## Stop conditions

- Large doc set with no clear owner: update only the section the user asked about; do not rewrite everything.
- Sensitive data (secrets, internal URLs): do not document in public-facing docs; note "configure per environment" or similar.

## Recovery

- If the doc location is ambiguous, propose one (e.g. `docs/feature-name.md`) and confirm with the user.

## Guardrails

- **Privacy:** Never document secrets, internal URLs, or credentials in public-facing docs. Use "configure per environment" for sensitive values.
- **Credentials:** Never hardcode credentials; use placeholder or env var reference.
- **Scope:** Do not expose paths, hostnames, or org-specific identifiers in shared artifacts unless user explicitly requests.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.

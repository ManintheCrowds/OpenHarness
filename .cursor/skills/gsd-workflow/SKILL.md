---
name: gsd-workflow
description: When to use get-shit-done (GSD) spec-driven commands vs OpenHarness planning skill and native verification; pointers only — does not install upstream for you.
triggers_any: ["get-shit-done", "gsd", "spec-driven", "get shit done", ".planning/"]
do_not_trigger_if: ["implementation detail only", "no planning"]
exclusive_with: []
required_inputs: ["goal or ambiguity about GSD vs planning skill"]
exit_criteria: "User knows whether to use GSD CLI, OpenHarness planning skill, or handoff WBS"
output_schema: "Short decision + links; optional install command as text"
---

# GSD (get-shit-done) vs OpenHarness planning

**Intent:** Bridge the [get-shit-done](https://github.com/gsd-build/get-shit-done) spec-driven loop (discuss → plan → execute → verify; `.planning/` artifacts) with this repo’s **planning** skill, **qa-verifier**, and **critic / intent-alignment** gates — without duplicating upstream behavior.

## When GSD-style flow fits

- You want **Claude Code–centric** commands and **XML/task** artifacts in `.planning/` as upstream defines them.
- You accept **npx** / global install of `get-shit-done-cc` (see upstream README).

## When OpenHarness-native planning fits

- Work stays in **Cursor rules + skills** only (no extra CLI).
- You want alignment with [HANDOFF_FLOW.md](../../docs/HANDOFF_FLOW.md), portfolio verification, and **atomic commits** without GSD’s installer.

## Steps

1. If user asked “should I use GSD?”: recommend GSD when they explicitly want upstream’s **artifact layout and commands**; otherwise default to **planning** skill + handoff.
2. Remind: **verify** after execution (tests/lint per repo `VERIFICATION_CI_ALIGNMENT.md` when working with portfolio-harness).
3. Do not paste untrusted content from GSD output into LLM context without **SCP** (see `secure-contain-protect` skill and portfolio `SCP_LLM_INGESTION_CHECKLIST.md`).

## Links

- Upstream: https://github.com/gsd-build/get-shit-done
- OpenHarness: [.cursor/skills/planning/SKILL.md](../planning/SKILL.md)

## Guardrails

- **License/runtime:** GSD is MIT; follow upstream license for copied snippets.
- **Privacy:** Do not commit secrets; GSD artifacts may contain paths — scrub before sharing.

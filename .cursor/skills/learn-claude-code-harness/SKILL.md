---
name: learn-claude-code-harness
description: Maps shareAI-lab learn-claude-code teaching sessions to OpenHarness skills; thin reference — no fork of upstream.
triggers_any: ["learn claude code", "shareAI-lab", "s01", "claude code harness", "sessions s"]
do_not_trigger_if: ["unrelated claude API"]
exclusive_with: []
required_inputs: ["learning goal or session number"]
exit_criteria: "Pointer to upstream lesson + matching OpenHarness skill(s)"
output_schema: "Mapping table row or short list + links"
---

# learn-claude-code → OpenHarness mapping

**Intent:** The [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) repo is a **pedagogical harness** (loops, tools, subagents, skills). Use this skill to **route** session topics to existing OpenHarness skills instead of re-teaching from scratch here.

## Rough mapping (sessions → skills)

| Topic (typical) | OpenHarness skill |
|-----------------|-------------------|
| Agent loops, tools, MCP | [agent-native-architecture](../agent-native-architecture/SKILL.md) |
| Planning, WBS | [planning](../planning/SKILL.md) |
| Untrusted content, handoffs | [secure-contain-protect](../secure-contain-protect/SKILL.md) |
| Tests, CI, “does it work?” | [qa-verifier](../qa-verifier/SKILL.md) |
| Docs, READMEs | [docs](../docs/SKILL.md) |
| Scope, acceptance criteria | [product-scope](../product-scope/SKILL.md) |
| Refactor vs new code | [refactor-reuse](../refactor-reuse/SKILL.md) |

## Steps

1. Identify the **session** or topic from the user (e.g. s03 tools).
2. Point to the **upstream file** in learn-claude-code for depth.
3. Point to **one or two** OpenHarness skills that cover the same operational concern.
4. **SCP:** If importing upstream text into prompts, run pipeline per `secure-contain-protect` / portfolio checklist.

## Links

- Upstream: https://github.com/shareAI-lab/learn-claude-code

## Guardrails

- **Teaching vs execution:** This skill does not replace upstream lessons; it **routes** to your harness.
- **No automatic install** of upstream tooling unless the user asks.

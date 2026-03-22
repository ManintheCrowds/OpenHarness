# Brainstorm: Code intelligence survey (arXiv 2511.18538) + harness alignment

**Date:** 2026-03-22  
**Status:** Captured (digest outline; see [gap analysis](../research/2511.18538-harness-gap-analysis.md)).

## What we are building (this effort)

A **structured digest** of the survey, an **OpenHarness gap analysis**, and an **intent-alignment gate** rule that complements the existing critic loop (quality vs. fit-to-intent).

## Paper (provenance)

- **Title:** From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence  
- **Identifier:** arXiv:2511.18538v5 [cs.SE] (6 Dec 2025); [Hugging Face Papers](https://hf.co/papers/2511.18538)  
- **Pages:** 303 (full PDF). **Canonical copy in repo:** [docs/research/2511.18538v5.pdf](../research/2511.18538v5.pdf). Optional text extract for search: `docs/research/_extract*.txt` (gitignored).

## Section map (top-level TOC)

| Sec | Title | Theme tags |
|-----|--------|--------------|
| 1 | Introduction | intent, deployment, history |
| 2 | Code Foundation Models | models, data, pre-training |
| 3 | Code Tasks, Benchmarks, and Evaluation | evaluation, LLM-as-judge, agents |
| 4 | Alignment | SFT, RL, multilingual, safety alignment |
| 5 | Software Engineering Agents | SWE agents, lifecycle, training |
| 6 | Code for Generalist Agents | MCP, tools, multi-agent, memory |
| 7 | Safety of Code LLMs | pre/post-training safety, red team, **intent grounding** (7.4.3) |
| 8 | Training Recipes | infra, PEFT, RL recipes |
| 9 | Applications | IDE, cloud, terminal agents, PR review |
| 10 | Contributions and Acknowledgements | — |

## Claims we care about (harness-relevant)

1. **Human intent and executable code** — The introduction frames NL intent → code as the central shift; aligns with [INTENT_ENGINEERING.md](../INTENT_ENGINEERING.md) (intent as primary signal).  
2. **Research vs. practice gap** — Benchmarks vs. real tasks (correctness, security, large-repo context, IDE workflows); aligns with our **verify-not-trust** and handoff/context discipline.  
3. **LLM-as-a-judge** — Used for evaluation in the survey; parallels our **critic JSON** (model-as-judge on outputs), not identical to training-time judges.  
4. **Agentic systems** — Tool use, benchmarks, terminal/UI agents; overlaps with **MCP**, agent-native architecture references, and role-routing.  
5. **Runtime oversight and intent grounding** (§7.4.3) — Closest paper anchor to **intent-alignment gate** (drift from stated user intent at inference time).

## Key decisions

- **PDF:** Canonical survey PDF lives in-repo at [docs/research/2511.18538v5.pdf](../research/2511.18538v5.pdf); gitignored `_extract*.txt` remains optional for chunked search/RAG.  
- **Critic** = artifact quality; **intent-alignment JSON** = alignment to user intent and constraints (orthogonal).  
- Document gaps and **value-add patterns** in [2511.18538-harness-gap-analysis.md](../research/2511.18538-harness-gap-analysis.md).

## Open questions

- Whether to ingest chunks into RAG (campaign_kb / Daggr) — only if you need cross-paper retrieval; default **no** (YAGNI).  
- Threshold for `drift_score` escalation — leave to human preference; document as optional in rule.

## Resolved questions

- **OA:** Preprint on arXiv/HF; Unpaywall optional if a DOI is assigned later.

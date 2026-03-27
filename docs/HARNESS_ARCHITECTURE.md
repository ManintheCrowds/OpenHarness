# Harness Architecture

The AI harness—surrounding infrastructure, integrations, memory management—often matters more than the underlying model. The same model can score 78% with one harness and 42% with another.

**Source:** Kapoor (CORE-Bench/HAL); Baitch, [The Model vs. the Harness](https://medium.com/@adambaitch/the-model-vs-the-harness-which-actually-matters-more-59dd3116bb31).

---

## Philosophy

**Collaboration model:** AI has access to local machine, manages state via structured artifacts, focuses on incrementalism.

**Harness > model:** Models converge; harnesses determine effectiveness.

---

## Known Failure Modes

**Inverted U-shaped performance:** Agent performance is often worst at extremes (rare domains, clinical extremes, adversarial inputs). Adequate on common cases; failures at edges. Validate agent behavior at extremes before relying on it for high-stakes decisions.

**Identify but advise wrong:** Models can correctly identify risk in their reasoning but still advise the wrong action (e.g., triage to "wait" instead of emergency). Human gates required for high-stakes outputs.

---

## What the Harness Is

| Component | Role |
|-----------|------|
| **Rules** | Operating principles, tool limits, skill routing |
| **Skills** | Per-task instructions; JIT-loaded |
| **state/** | Institutional memory: handoff, decision-log, known-issues, preferences |
| **Handoff** | "Document then continue" — Done/Next, archive, continue prompt |
| **MCP** | Model Context Protocol servers for tools and resources |

---

## External benchmarks and sims (implementation-side)

Multi-agent sims, prompt-eval harnesses, and benchmark runners **do not live in OpenHarness core**. They belong in **implementation repos** (research notes, optional automation, MCP wrappers) per [DELINEATION.md](DELINEATION.md). The harness still **points** to them so operators know where runbooks and provenance live.

**Examples (sibling-repo layout; adjust paths if your clone differs):**

| Topic | Canonical write-up |
|-------|-------------------|
| DECIDE-SIM stack placement (OpenAtlas vs research vs local-proto) | [portfolio-harness brainstorm](../../portfolio-harness/docs/brainstorms/2026-03-20-decide-sim-stack-integration-brainstorm.md) |
| Paper note + meditation backlog | [software research note](../../software/docs/research/arxiv_2509.12190_DECIDE_SIM.md) |
| Promptfoo vs DECIDE-SIM (gap analysis) | [promptfoo_vs_DECIDE_SIM_gap_analysis.md](../../software/docs/research/promptfoo_vs_DECIDE_SIM_gap_analysis.md) |

**Convention:** Consume **summaries + hashes + SCP** on excerpts—not raw API dumps in core docs. Optional operator UI (e.g. OpenAtlas) reads **pre-computed JSON** only; execution stays outside the Next app—see [OPENATLAS_SYSTEMS_INVENTORY.md](../../portfolio-harness/OpenAtlas/docs/OPENATLAS_SYSTEMS_INVENTORY.md) in a sibling **portfolio-harness** checkout.

---

## Memory

**Load order (new session):**

1. intent_surface.md (if exists)
2. session_brief.md (if exists)
3. handoff_latest.md
4. preferences.md
5. rejection_log.md (if proposing similar work)
6. decision-log.md (if exists)
7. known-issues.md (if exists)
8. daily/YYYY-MM-DD.md (optional)

See [SESSION_BOOTSTRAP.md](SESSION_BOOTSTRAP.md) for the same sequence with links. See [OPENHARNESS_CONTEXT_MAP.md](OPENHARNESS_CONTEXT_MAP.md) for checklist → path mapping.

## Agent-native maintenance

After **large** changes to `.cursor/skills/` (new folders, major SKILL.md edits), run `python scripts/verify_skills_readme.py` and optionally an agent-native audit ([.cursor/commands/agent-native-audit.md](../.cursor/commands/agent-native-audit.md)) so discovery and parity docs stay aligned.

---

## Lock-in

This harness is **Cursor-centric**. Portable: state schema, handoff format, plan structure. Cursor-specific: .cursorrules, role-routing, MCP config.

## Public vs private

OpenHarness is intended as a **public reference**: patterns and **synthetic** examples, not real operator handoffs or internal state. Keep real `handoff_*`, `daily/`, and credential-backed workflows in **private** repos. See [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md) and [examples/HANDOFF_EXAMPLE_SYNTHETIC.md](examples/HANDOFF_EXAMPLE_SYNTHETIC.md).

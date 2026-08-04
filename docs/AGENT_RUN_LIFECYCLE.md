# Agent-run lifecycle

**Status:** Guide stub (public)  
**Taxonomy home:** OpenHarness  
**Axis:** Working-partner continuity — **not** Patient “retirement,” **not** Content quarantine purge.

Companion: [PATIENT_THREAT_CONTENT_DELINEATION.md](PATIENT_THREAT_CONTENT_DELINEATION.md) · [THREE_CANDORS.md](THREE_CANDORS.md) (Intent candor).

---

## Stages

| Stage | What happens | Typical artifacts |
|-------|----------------|-------------------|
| **1. Bootstrap** | Load intent, handoff, preferences, rejection_log, decision-log, known-issues (session bootstrap order) | `state/`, continue prompt, capability manifest |
| **2. Active work** | Forward passes / tool use under critic + intent-alignment gates; HITL when required | Working tree, async tasks, Sync Session / Alignment Context (if OpenGrimoire) |
| **3. Handoff archive** | Document-then-continue: archive prior handoff, write `handoff_latest`, daily / decision_index as applicable | Handoff body, continue prompt refresh |
| **4. Terminate** | Session or run ends; **no ongoing model “stream of consciousness”** while idle — next turn is a new forward pass over context | Persisted `state/` only |

Swarm variant (multi-role runs): see [SWARM_OPERATING_MODES.md](SWARM_OPERATING_MODES.md) § Minimal run lifecycle (initialize run artifact → proposals/critiques → referee → human gate → finalize + handoff note). This doc is the **session-level** frame; swarm is a specialized run inside stage 2–3.

Full portable procedure: [HANDOFF_FLOW.md](HANDOFF_FLOW.md). Do not duplicate archive scripts here.

---

## What persists vs what dies

| Survives terminate | Does not survive as a living process |
|--------------------|--------------------------------------|
| Handoff archive, decision-log, preferences, rejection_log, daily notes | An idle chat window “waiting” with continuous inner life |
| Brain-map / context graph JSON derived from state | A particular GPU forward-pass instance |
| Continue prompt for the next agent | Unwritten intent (if never handed off) |

Berg/Harris “anesthesia between turns” maps here as **no active processing when idle** — a description of how current LLM sessions work, not a Patient-axis sanctuary policy.

---

## Explicit non-claims

- Agent-run lifecycle is **work continuity** for operators and Guide agents — not model-instance welfare or “retirement home” ethics.
- Ending a session / deprecating a product model version is **ops** (and may touch Content lifecycle for quarantined blobs); it is not automatically a Patient decision.
- Quarantine purge (`scp_purge_quarantine`) is a **different lifecycle** — see SCP [QUARANTINE_LIFECYCLE.md](https://github.com/ManintheCrowds/SCP/blob/main/docs/QUARANTINE_LIFECYCLE.md).

---

## See also

- [SESSION_BOOTSTRAP.md](SESSION_BOOTSTRAP.md)
- [ASYNC_HITL_SCOPE.md](ASYNC_HITL_SCOPE.md)
- [PUBLIC_AND_PRIVATE_HARNESS.md](PUBLIC_AND_PRIVATE_HARNESS.md) — real handoffs stay private

**Risk:** Low (documentation). Rollback: delete this file and revert pointers.

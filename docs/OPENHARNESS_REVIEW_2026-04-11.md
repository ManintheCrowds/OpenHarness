# OpenHarness review — intent, context, process status (2026-04-11)

## Goal under review

Target product goal (from user directive): **OpenHarness as an agnostic template for operating AI agents and AI swarm decision-making processes**.

## Verified intent and context

### What OpenHarness already is

- A **portable harness** focused on context engineering, intent engineering, handoff flow, and state schema (not a monolithic runtime framework).
- Explicitly positioned as **model-agnostic / platform-portable patterns** with Cursor-centric defaults but portable core primitives.
- Uses a **verify-not-trust** philosophy with script/YAML parity checks and canonical bundle hashing.

### Core architectural pillars in-repo

1. **Intent-first operations** (intent, scope, constraints, human gate, latency).
2. **Structured memory/state schema** (`state/`) for continuity across sessions and agents.
3. **Document-then-continue handoff protocol** with explicit Done/Next and archive rules.
4. **Operational guardrails** via checklists, scripts, and CI verification.
5. **Async / HITL compatibility** through machine-readable task ledger (`async_tasks.yaml`) and ownership semantics.

### Agnostic + swarm-readiness signals already present

- Async multi-session orchestration concepts exist (`docs/ASYNC_HITL_SCOPE.md`, `state/async_tasks.yaml`).
- Intent schema and human-gate semantics are already designed for delegated, multi-step work.
- Delineation docs keep core harness independent from app-specific implementations.

## Where we are in the development process

## Phase assessment

OpenHarness appears to be in a **mature architecture/specification hardening phase** for a public reference harness, with:

- Strong core docs and schemas in place.
- Foundational verification scripts in place.
- Public-safe placeholders for operational state.
- A small backlog item focused on parity tooling (thin MCP wrapper).

Not yet a full “batteries-included” swarm runtime; currently a **governance + process substrate** that can host one.

## Current status indicators

- Latest handoff (2026-03-26) indicates async/HITL roadmap artifacts were added and verification integrated.
- Backlog has one explicit future item: thin MCP wrapper for allowlisted script invocation.
- Decision and known-issues logs are still intentionally minimal/public-safe placeholders.

## Gaps relative to your stated north star

To fully satisfy “agnostic template for operating AI agents and AI swarm decision-making,” the largest gaps are:

1. **Reference swarm control loop spec**
   - Need a canonical pattern for planner/critic/executor/referee roles and arbitration strategy.

2. **Swarm decision protocol contract**
   - Need machine-readable schema for proposals, votes/scores, tie-breakers, and confidence/risk annotations.

3. **Policy profiles by risk tier**
   - Need preset governance profiles (low/medium/high stakes) mapping human gates and escalation triggers.

4. **Interoperability adapters**
   - Need lightweight adapters/examples for non-Cursor environments while preserving core schema.

5. **Evaluation harness for collective quality**
   - Need benchmark tasks and acceptance metrics for single-agent vs multi-agent outcomes.

## Recommended next steps (ordered)

1. **Define v0.1 Swarm Decision Contract**
   - Add `docs/contracts/swarm_decision_v0_1.md` (proposal schema, scoring fields, arbitration fields, final-decision envelope).

2. **Publish a canonical “Swarm Operating Modes” doc**
   - Add `docs/SWARM_OPERATING_MODES.md` covering at least:
     - single-agent
     - planner/executor
     - planner/critic/executor
     - N-agent quorum with referee

3. **Extend state schema for swarm runs**
   - Add optional artifacts like `state/swarm_runs/YYYY-MM-DD/<run-id>.md` and/or YAML summaries compatible with existing handoff flow.

4. **Add verification script for swarm artifacts**
   - Add `scripts/verify_swarm_contract.py` to enforce required fields and prevent silent format drift.

5. **Add 2-3 synthetic end-to-end examples**
   - Include one low-risk and one high-risk scenario with explicit human gate behavior and async handoff continuity.

6. **Create roadmap milestones**
   - Convert the above into milestones (M1 schema, M2 examples, M3 verification, M4 adapters).

## Alignment decisions (captured)

Resolved product decisions:

1. **Primary audience first:** Optimize first for **solo builders**.
2. **Swarm topology baseline:** Adopt **one default topology**.
3. **Decision semantics:** Use **referee override** as the default final decision rule.
4. **Risk posture:** For high-stakes use, **irreversible actions always require a human gate**.
5. **Execution scope:** Include a **minimal runnable orchestrator reference** in OpenHarness.

Still-open strategic questions:

1. **Platform priority:** Which non-Cursor target should come first (CLI-only, GitHub Actions, LangGraph, OpenAI Responses tools, others)?
2. **Success metric:** What defines “v1 ready” first—adoption, reliability, eval gains, or governance completeness?

## Suggested immediate decision

Given the resolved decisions above, recommended immediate spike order:

1. **A:** Swarm Decision Contract first (schemas + validation).
2. **B:** Swarm Operating Modes (single default topology with referee override encoded as default policy).
3. **C:** Minimal runnable orchestrator reference that enforces mandatory human gate for high-stakes irreversible actions.

After A/B/C, draft the exact file set and acceptance tests for a “solo-builder-first v0.1” release slice.

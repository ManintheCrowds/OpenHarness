# Swarm Operating Modes (v0.1)

This document defines portable operating modes for OpenHarness. For v0.1, the default mode is:

- `planner_critic_executor_referee`
- default decision rule: `referee_override`

## Coordination class (v0.1)

All catalog modes below are **scripted role-envelope** coordination: fixed roles, sequential proposals/critique/arbitration (or single-agent end-to-end), plus handoff/run artifacts. They are **not** **collaborative swarm** (dynamic role assignment, local custody handoff, self-orchestration without a fixed referee script).

v0.1 does not implement collaborative self-orchestration. Mutualistic threat-intel / mycelium-style registries are orthogonal to this catalog—not an operating mode here.

## Mode catalog

## 1) `single_agent`

- One agent executes end-to-end.
- Use for low-complexity, low-risk tasks.

## 2) `planner_executor`

- Planner proposes steps; executor implements.
- Use for medium complexity when critique overhead is unnecessary.

## 3) `planner_critic_executor`

- Critic reviews plan/implementation before finalization.
- Use when quality assurance is needed but formal arbitration is not.

## 4) `planner_critic_executor_referee` (default)

- Planner proposes options.
- Critic identifies risk and weakness.
- Executor provides implementation feasibility and constraints.
- Referee performs final arbitration and may override by policy.

## High-stakes policy

If an action is both high-stakes and irreversible:

1. set `human_gate_required: true`
2. block finalization until approval is recorded
3. persist approval reference in run artifacts and handoff

## Future class: collaborative swarm (not implemented)

**collaborative swarm** is a non-implemented coordination class. Do not claim v0.1 modes satisfy it.

Directional entry criteria before labeling a run collaborative (do not invent runtime in this doc):

1. Runnable orchestration beyond synthetic `state/swarm_runs/` schema theater
2. Dynamic role or custody handoff without a fixed referee script as the only arbiter
3. Honest operator-on-the-loop policy (process/host HITL—not assumed machine-enforced)

Until those hold, keep using scripted role-envelope labels for the modes above.

## Minimal run lifecycle

1. Initialize run artifact (`state/swarm_runs/...`).
2. Collect proposals and critiques.
3. Referee arbitration and tentative winner.
4. Enforce human gate policy if applicable.
5. Finalize decision, write audit trail, append handoff note.

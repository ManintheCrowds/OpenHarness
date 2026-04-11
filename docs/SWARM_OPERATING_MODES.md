# Swarm Operating Modes (v0.1)

This document defines portable operating modes for OpenHarness. For v0.1, the default mode is:

- `planner_critic_executor_referee`
- default decision rule: `referee_override`

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

## Minimal run lifecycle

1. Initialize run artifact (`state/swarm_runs/...`).
2. Collect proposals and critiques.
3. Referee arbitration and tentative winner.
4. Enforce human gate policy if applicable.
5. Finalize decision, write audit trail, append handoff note.

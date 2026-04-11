# Swarm Decision Contract v0.1 (synthetic/public)

Status: draft-v0.1

Purpose: provide a portable, machine-readable envelope for multi-agent proposals, scoring, arbitration, and final decision output.

## Decision envelope

Required top-level fields:

- `contract_version`: `swarm_decision_v0_1`
- `run_id`: unique id for one swarm decision run
- `intent`: one-line target objective
- `mode`: operating mode id (see `docs/SWARM_OPERATING_MODES.md`)
- `decision_rule`: `referee_override` (default policy)
- `high_stakes`: boolean
- `irreversible_action`: boolean
- `human_gate_required`: boolean
- `status`: `draft | finalized | blocked_human_gate | aborted`
- `proposals`: list of agent proposals
- `arbitration`: referee evaluation + rationale
- `final_decision`: selected proposal + reason + confidence
- `audit`: timestamps and provenance

## Proposal object

Each entry in `proposals[]` must include:

- `proposal_id`
- `agent_id`
- `summary`
- `plan_steps` (ordered list)
- `risks` (list)
- `confidence` (0.0-1.0)
- `evidence` (paths/links)
- `constraints_checked` (list)

## Arbitration object

Required fields:

- `referee_agent_id`
- `scores` (map: proposal_id -> score)
- `winner_proposal_id`
- `override_applied` (boolean)
- `rationale`
- `dissent_notes` (optional list)

## Human gate policy

Normative rule for v0.1:

- If `high_stakes=true` and `irreversible_action=true`, then `human_gate_required` MUST be `true`.
- When `human_gate_required=true`, `status` MUST be `blocked_human_gate` until approval is recorded.

## YAML example (minimal)

```yaml
contract_version: swarm_decision_v0_1
run_id: swarm-20260411-001
intent: Select rollout strategy for docs-only migration.
mode: planner_critic_executor_referee
decision_rule: referee_override
high_stakes: false
irreversible_action: false
human_gate_required: false
status: finalized
proposals:
  - proposal_id: p1
    agent_id: planner
    summary: Stage changes over two weekly releases.
    plan_steps: ["prepare", "announce", "rollout"]
    risks: ["schedule slip"]
    confidence: 0.74
    evidence: ["docs/BACKLOG.md"]
    constraints_checked: ["public-safe", "no-secrets"]
arbitration:
  referee_agent_id: referee
  scores: {p1: 0.82}
  winner_proposal_id: p1
  override_applied: false
  rationale: Best tradeoff of risk and speed.
final_decision:
  selected_proposal_id: p1
  reason: Highest referee score with acceptable risk.
  confidence: 0.82
audit:
  created_at: 2026-04-11T00:00:00Z
  finalized_at: 2026-04-11T00:15:00Z
  sources: ["docs/SWARM_OPERATING_MODES.md"]
```

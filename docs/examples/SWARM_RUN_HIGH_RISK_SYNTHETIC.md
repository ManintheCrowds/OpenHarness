# Synthetic swarm run example — high risk

- Run id: `swarm-20260411-highrisk`
- Intent: evaluate irreversible data purge
- Mode: `planner_critic_executor_referee`
- Decision rule: `referee_override`
- Human gate: required (`high_stakes=true`, `irreversible_action=true`)

## Outcome

Referee produced a tentative winner, but the run remains `blocked_human_gate` pending explicit approval.

## Artifact

- `state/swarm_runs/2026-04-11/swarm-20260411-highrisk.yaml`

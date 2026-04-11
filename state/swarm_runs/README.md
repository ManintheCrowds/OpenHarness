# Swarm run artifacts (synthetic/public schema)

Store machine-readable summaries for swarm decisions.

## Layout

- `state/swarm_runs/YYYY-MM-DD/<run-id>.yaml`
- Optional narrative companion: `state/swarm_runs/YYYY-MM-DD/<run-id>.md`

## YAML required fields (v0.1)

- `contract_version`
- `run_id`
- `intent`
- `mode`
- `decision_rule`
- `high_stakes`
- `irreversible_action`
- `human_gate_required`
- `status`
- `proposals`
- `arbitration`
- `final_decision`
- `audit`

## Policy constraint

When `high_stakes: true` and `irreversible_action: true`, then `human_gate_required` must be `true`.

Use `python scripts/verify_swarm_contract.py` to validate YAML artifacts.

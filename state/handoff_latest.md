decision_id: handoff-20260326-async-hitl-harness
Updated: 2026-03-26T15:00:00Z

## Done

- **Async / multi-session harness roadmap (public-safe summary):** Added [docs/ASYNC_HITL_SCOPE.md](../docs/ASYNC_HITL_SCOPE.md) (task ids, statuses, ownership, conflict rules, HITL semantics).
- **Machine-readable ledger:** [state/async_tasks.yaml](async_tasks.yaml) (synthetic example task) + [scripts/verify_async_tasks.py](../scripts/verify_async_tasks.py); wired into `verify` job in [.github/workflows/ci.yml](../.github/workflows/ci.yml).
- **Security:** Gitleaks job + [.gitleaks.toml](../.gitleaks.toml) in CI; residual history risk documented in ASYNC_HITL_SCOPE.
- **Cross-links:** [state/README.md](README.md), [docs/SESSION_BOOTSTRAP.md](../docs/SESSION_BOOTSTRAP.md), [docs/HARNESS_ARCHITECTURE.md](../docs/HARNESS_ARCHITECTURE.md), [docs/CHEATSHEET.md](../docs/CHEATSHEET.md), [docs/OPENHARNESS_CONTEXT_MAP.md](../docs/OPENHARNESS_CONTEXT_MAP.md), [capabilities.harness.yaml](../capabilities.harness.yaml).

## Next

- Push branch and confirm GitHub Actions: `verify` (including `verify_async_tasks.py`) and `gitleaks` both green.
- When doing real async work: replace or extend `async_tasks.yaml` rows (keep ids unique); set `latency_tolerance: async_ok` in handoff and read the ledger after narrative handoff.

## Paths / artifacts

- [docs/ASYNC_HITL_SCOPE.md](../docs/ASYNC_HITL_SCOPE.md)
- [state/async_tasks.yaml](async_tasks.yaml)
- [scripts/verify_async_tasks.py](../scripts/verify_async_tasks.py)
- [.github/workflows/ci.yml](../.github/workflows/ci.yml)

## Verification commands run

- `python scripts/verify_async_tasks.py` — pass
- `python scripts/verify_script_index.py` — pass
- `python scripts/verify_contract_hash.py` — pass
- Docker `gitleaks detect` with repo `.gitleaks.toml` — no leaks found (local)

## scope

OpenHarness public reference; no consumer-app or MCP runtime changes.

## latency_tolerance

async_ok

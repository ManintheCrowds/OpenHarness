#!/usr/bin/env python3
"""Validate swarm run YAML artifacts against OpenHarness v0.1 contract requirements.

Note: this verifier intentionally avoids third-party dependencies so it can run in
minimal environments.
"""

from __future__ import annotations

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SWARM_ROOT = REPO_ROOT / "state" / "swarm_runs"

REQUIRED_TOP_LEVEL = {
    "contract_version",
    "run_id",
    "intent",
    "mode",
    "decision_rule",
    "high_stakes",
    "irreversible_action",
    "human_gate_required",
    "status",
    "proposals",
    "arbitration",
    "final_decision",
    "audit",
}


def validate_yaml(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    top_keys = set()
    top_values: dict[str, str] = {}
    for raw_line in text.splitlines():
        if not raw_line or raw_line.startswith(" ") or raw_line.startswith("\t"):
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        if not key:
            continue
        top_keys.add(key)
        top_values[key] = value.strip()

    missing = sorted(REQUIRED_TOP_LEVEL - top_keys)
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")

    if top_values.get("contract_version") != "swarm_decision_v0_1":
        errors.append(f"{path}: contract_version must be 'swarm_decision_v0_1'")

    if top_values.get("decision_rule") != "referee_override":
        errors.append(f"{path}: decision_rule must be 'referee_override' for v0.1")

    high_stakes = top_values.get("high_stakes") == "true"
    irreversible = top_values.get("irreversible_action") == "true"
    gate = top_values.get("human_gate_required") == "true"
    status = top_values.get("status")

    if high_stakes and irreversible and not gate:
        errors.append(
            f"{path}: human_gate_required must be true when high_stakes and irreversible_action are true"
        )

    if gate and status not in {"blocked_human_gate", "finalized"}:
        errors.append(
            f"{path}: status must be blocked_human_gate or finalized when human_gate_required is true"
        )

    if top_values.get("proposals") is None:
        errors.append(f"{path}: proposals must be a non-empty list")

    return errors


def main() -> int:
    yaml_files = sorted(SWARM_ROOT.rglob("*.yaml"))
    if not yaml_files:
        print(f"No swarm YAML artifacts found under {SWARM_ROOT}")
        return 0

    errors: list[str] = []
    for file_path in yaml_files:
        errors.extend(validate_yaml(file_path))

    if errors:
        print("Swarm contract verification failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Swarm contract verification passed ({len(yaml_files)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

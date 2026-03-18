---
name: qa-verifier
description: Use when running tests, verifying behavior, checking "does it work?", reproducing bugs, or validating a change. Use for test runs, CI-style checks, and acceptance verification. Load when the user asks to test, verify, or validate.
triggers_any: ["run tests", "verify", "validate", "does it work", "reproduce", "acceptance", "test", "pytest", "npm test"]
do_not_trigger_if: ["evaluate quality only", "critic report only", "documentation only"]
exclusive_with: []
required_inputs: ["what to verify (test command, path, or scenario)", "repo or workspace context"]
forbidden_actions: ["edit code during verification run", "run destructive or out-of-scope commands"]
exit_criteria: "Pass/fail stated; failing tests or steps listed; summary one to three lines."
output_schema: "Report: command(s) run; result PASS/FAIL; failing items; summary."
---

# QA / Verifier role

**Intent:** Run tests, repro steps; report pass/fail—does it work?

## When to use

- User asks to run tests, verify, validate, or check behavior.
- After implementing a fix or feature; before marking work "done."
- When reproducing a bug or checking acceptance criteria.

## Inputs

- What to verify: specific test command, path, or scenario.
- Repo/workspace context (which project, which test runner).

## Verification types

| Type | Description | Examples |
|------|-------------|----------|
| **static** | Lint, schema validation, type checking. No execution. | ruff, eslint, mypy, JSON schema, OpenAPI validate |
| **semantic** | Behavior claims vs code: do assertions or docs match implementation? | Spot-check "X does Y" in code; compare README to actual CLI flags |
| **diff** | Change impact surface: what files or call sites are affected? | git diff --name-only; grep for callers of changed symbol |
| **dependency** | New imports, licenses, vulnerable deps. | pip-audit, npm audit, new require/import list |
| **runtime** | Tests, build, or repro steps. | pytest, npm test, cargo test, manual repro |

## Matrix (artifact type → verification types)

| Artifact type | Recommended types | Notes |
|---------------|--------------------|--------|
| code (application) | static, runtime, dependency | Always run tests; add static if linter exists; dependency on new deps. |
| code (library/API) | static, runtime, semantic | Add semantic if API contract or docs claim behavior. |
| docs only | semantic | Do claims in docs match code? Optional. |
| rules / skills | static (syntax) | Validate syntax; consider manual review for security. |
| config / schema | static | Validate schema or config format. |
| migration / DB | static, diff, runtime | Diff for impact; runtime for migration script if applicable. |

When in doubt, run at least **runtime** (tests) for code and **static** where the project has lint/schema. Add **dependency** when the change adds or updates dependencies.

## Tool output limits

Apply these limits to avoid serialization errors and leaking large logs:

- **Terminal:** Bash: `| head -50` or `| tail -100`; PowerShell: `| Select-Object -First 20`. Use `--max-count`, `-maxdepth`, or filtering flags.
- **File reading:** Check size first; use `read_file(path, offset=0, limit=100)` for large files. For logs: `tail -n 100` first.
- **Grep:** Use `output_mode: "files_with_matches"` when possible; add `head_limit: 20`.

## Steps

1. **Identify** the right verification: from the matrix, pick types for the artifact (e.g. code → runtime + static; rules → static).
2. **Run** the relevant tests or commands. Apply tool output limits above.
3. **Report** clearly: passed / failed; if failed, list failing tests or steps and a one-line summary of cause if obvious.

## Checks

- Tests actually ran (not skipped or missing).
- Output is summarized; no giant logs unless the user asks.
- Pass/fail and failing test names (or repro steps) are explicit.

## Stop conditions

- Tests require env (e.g. DB, API key) that is not available: stop and tell the user what is needed.
- More than a few tests fail: report and stop; do not auto-fix unless the user asked to fix failures.

## Recovery

- If the test command is unknown, list likely commands (e.g. `pytest`, `npm test`) and ask the user which to run, or run the one that matches the project type.

## Guardrails

- **Scope:** Do not expose paths, hostnames, or org-specific identifiers in shared artifacts unless user explicitly requests.
- **Human gate:** Escalate when uncertain; do not auto-resolve conflicts between roles.

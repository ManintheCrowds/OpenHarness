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

# QA-verifier (delegated)

**Canonical skill (edit there):** [MiscRepos `qa-verifier` SKILL](../../../MiscRepos/.cursor/skills/qa-verifier/SKILL.md)

See [product-scope SKILL](../product-scope/SKILL.md) header for delegation policy and sibling layout.

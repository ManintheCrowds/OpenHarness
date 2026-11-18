# PURPOSE: A planted synthetic handoff fails mask-check and gitleaks.
# The masked copy passes. Secrets stay in the allowlisted fixture file.

"""Proof test for the privacy pre-commit hooks."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import unittest
import urllib.request
from collections import Counter
from pathlib import Path

from scp.mask_secrets import mask

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".pre-commit-config.yaml"
GITLEAKS_TOML = ROOT / ".gitleaks.toml"
REQUIREMENTS = ROOT / "requirements.txt"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "handoff_planted_secret.md"

GITLEAKS_REV = "v8.30.1"
GITLEAKS_VERSION = "8.30.1"
GITLEAKS_COMMIT = "83d9cd684c87d95d656c1458ef04895a7f1cbd8e"
SCP_SHA = "6f8bcbdcb2c602b64f0d63b14a42897f8cf92d5a"

# Entry from gitleaks .pre-commit-hooks.yaml at tag v8.30.1 (id: gitleaks).
GITLEAKS_HOOK_ARGS = ["git", "--pre-commit", "--redact", "--staged", "--verbose"]


def _config_text() -> str:
    return CONFIG.read_text(encoding="utf-8")


def _mask_check_section() -> str:
    text = _config_text()
    marker = "id: mask-check"
    if marker not in text:
        raise AssertionError("mask-check hook missing")
    return text.split(marker, 1)[1].split("\n      - id:", 1)[0]


def _mask_check_argv() -> list[str]:
    match = re.search(r"^\s*entry:\s*(.+)$", _mask_check_section(), re.MULTILINE)
    if match is None:
        raise AssertionError("mask-check entry missing")
    argv = match.group(1).strip().split()
    if argv[0] != "python":
        raise AssertionError("mask-check entry must start with python")
    argv[0] = sys.executable
    return argv


def _mask_check_files() -> re.Pattern[str]:
    match = re.search(r"^\s*files:\s*'([^']+)'", _mask_check_section(), re.MULTILINE)
    if match is None:
        raise AssertionError("mask-check files pattern missing")
    return re.compile(match.group(1))


def _planted_values(raw: str) -> list[str]:
    values: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        if lower.startswith("email:") or lower.startswith("ssn:"):
            values.append(stripped.split(":", 1)[1].strip())
        elif "=" in stripped and not stripped.startswith("#"):
            values.append(stripped.split("=", 1)[1].strip())
    if not values:
        raise AssertionError("fixture has no planted values")
    return values


def _run(argv: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv,
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def _assert_values_hidden(proc: subprocess.CompletedProcess[str], values: list[str]) -> None:
    combined = proc.stdout + proc.stderr
    leaked = [value for value in values if value and value in combined]
    if leaked:
        raise AssertionError("hook output echoed a planted fixture value")


def _gitleaks_bin() -> Path:
    override = os.environ.get("GITLEAKS_BIN")
    if override:
        binary = Path(override)
        if not binary.is_file():
            raise AssertionError("GITLEAKS_BIN is not a file")
        return binary

    cache = Path.home() / ".cache" / "openharness" / f"gitleaks-{GITLEAKS_VERSION}-linux-x64"
    binary = cache / "gitleaks"
    if binary.is_file():
        return binary

    base = f"https://github.com/gitleaks/gitleaks/releases/download/{GITLEAKS_REV}"
    archive_name = f"gitleaks_{GITLEAKS_VERSION}_linux_x64.tar.gz"
    checksums = _fetch(f"{base}/gitleaks_{GITLEAKS_VERSION}_checksums.txt").decode("utf-8")
    archive_bytes = _fetch(f"{base}/{archive_name}")
    digest = hashlib.sha256(archive_bytes).hexdigest()
    expected = ""
    for line in checksums.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[-1].endswith(archive_name):
            expected = parts[0]
            break
    if not expected or expected != digest:
        raise AssertionError("gitleaks release checksum mismatch")

    cache.mkdir(parents=True, exist_ok=True)
    archive_path = cache / archive_name
    archive_path.write_bytes(archive_bytes)
    with tarfile.open(archive_path) as tar:
        member = tar.getmember("gitleaks")
        if member.name != "gitleaks" or not member.isfile():
            raise AssertionError("gitleaks archive layout unexpected")
        source = tar.extractfile(member)
        if source is None:
            raise AssertionError("gitleaks archive layout unexpected")
        with source, binary.open("wb") as dest:
            shutil.copyfileobj(source, dest)
    binary.chmod(binary.stat().st_mode | stat.S_IEXEC)
    return binary


def _fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "openharness-privacy-hook-test"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def _git(repo: Path, *args: str) -> None:
    proc = _run(["git", *args], repo)
    if proc.returncode != 0:
        raise AssertionError(f"git {' '.join(args)} failed")


def _entropy(text: str) -> float:
    counts = Counter(text)
    total = len(text)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def _synthetic_email() -> str:
    return "synthetic-user" + "@" + "example.com"


def _synthetic_ssn() -> str:
    return "-".join(("000", "00", "0000"))


def _synthetic_github_pat() -> str:
    """GitHub PAT-shaped token built at runtime so the source file does not store it."""
    prefix = "gh" + "p_"
    body = "".join(
        (
            "aB3k",
            "m9Qx",
            "Zp2L",
            "n8Wc",
            "R4tY",
            "u6Hs",
            "d1Jf",
            "q5Ve",
            "K7bN",
        )
    )
    token = prefix + body
    if not re.fullmatch(r"ghp_[0-9a-zA-Z]{36}", token):
        raise AssertionError("synthetic github pat has the wrong shape")
    if _entropy(token) < 3:
        raise AssertionError("synthetic github pat entropy is below the gitleaks minimum")
    return token


def _synthetic_aws_access_key() -> str:
    """AWS-shaped token built at runtime so the source file does not store it."""
    prefix = "AK" + "IA"
    body = "".join(("Q7M4", "N6P3", "R5WX", "2Y6K"))
    token = prefix + body
    if not re.fullmatch(r"AKIA[A-Z2-7]{16}", token):
        raise AssertionError("synthetic aws key has the wrong shape")
    if _entropy(token) < 3:
        raise AssertionError("synthetic aws key entropy is below the gitleaks minimum")
    if token.endswith("EXAMPLE"):
        raise AssertionError("synthetic aws key hits the gitleaks example allowlist")
    return token


def _init_repo(repo: Path) -> None:
    _git(repo, "init")
    shutil.copy(GITLEAKS_TOML, repo / ".gitleaks.toml")
    _git(repo, "add", ".gitleaks.toml")
    _git(
        repo,
        "-c",
        "user.email=privacy-hook-test@example.com",
        "-c",
        "user.name=privacy-hook-test",
        "commit",
        "-m",
        "baseline",
    )


def _gitleaks_findings(binary: Path, repo: Path) -> set[str]:
    report = repo / "gitleaks-report.json"
    proc = _run(
        [
            str(binary),
            "detect",
            "--redact",
            "--no-banner",
            "--config",
            str(repo / ".gitleaks.toml"),
            "--report-format",
            "json",
            "--report-path",
            str(report),
        ],
        repo,
    )
    if not report.is_file():
        raise AssertionError("gitleaks did not write a report")
    data = json.loads(report.read_text(encoding="utf-8") or "[]")
    report.unlink()
    files = {str(item.get("File", "")) for item in data}
    if proc.returncode == 0 and files:
        raise AssertionError("gitleaks reported files but exited 0")
    return files


class PrivacyHookTests(unittest.TestCase):
    def test_config_pins_gitleaks_mask_check_and_scp_sha(self) -> None:
        text = _config_text()
        self.assertIsNotNone(
            re.search(
                r"repo:\s*https://github.com/gitleaks/gitleaks\s+rev:\s*" + re.escape(GITLEAKS_COMMIT),
                text,
            )
        )
        self.assertIn("id: gitleaks", text)
        requirements = REQUIREMENTS.read_text(encoding="utf-8")
        self.assertIn(SCP_SHA, requirements)
        self.assertIn("TODO: repin scp-mcp to a main SHA", requirements)
        self.assertNotIn("scripts/mask_secrets.py", text)

        section = _mask_check_section()
        argv = _mask_check_argv()
        self.assertEqual(argv[1:], ["scripts/mask_check.py", "--check"])
        self.assertIn("stages: [pre-commit]", section)
        files_re = _mask_check_files()
        self.assertIsNotNone(files_re.search("state/handoff_latest.md"))
        self.assertIsNotNone(files_re.search("state/daily/note.json"))
        self.assertIsNotNone(files_re.search("state/session.jsonl"))
        self.assertIsNone(files_re.search("README.md"))
        self.assertIsNone(files_re.search("docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md"))
        self.assertIsNone(files_re.search("scripts/sanitize_input.py"))

    def test_planted_handoff_fails_mask_check_until_masked(self) -> None:
        raw = FIXTURE.read_text(encoding="utf-8")
        values = _planted_values(raw)
        rel = Path("state/handoff_planted.md")
        self.assertIsNotNone(_mask_check_files().search(rel.as_posix()))

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / rel
            target.parent.mkdir(parents=True)
            target.write_text(raw, encoding="utf-8")

            failed = _run([*_mask_check_argv(), str(target)], ROOT)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("SECRETS DETECTED", failed.stderr)
            _assert_values_hidden(failed, values)

            masked = mask(raw)
            for value in values:
                self.assertNotIn(value, masked)
            target.write_text(masked, encoding="utf-8")

            passed = _run([*_mask_check_argv(), str(target)], ROOT)
            self.assertEqual(passed.returncode, 0)
            self.assertIn("OK: No secrets detected", passed.stdout)
            _assert_values_hidden(passed, values)

    def test_planted_handoff_fails_gitleaks_hook_until_masked(self) -> None:
        binary = _gitleaks_bin()
        version = _run([str(binary), "version"], ROOT)
        self.assertEqual(version.returncode, 0)
        self.assertIn(GITLEAKS_VERSION, version.stdout + version.stderr)

        raw = FIXTURE.read_text(encoding="utf-8")
        values = _planted_values(raw)
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            _init_repo(repo)

            planted = repo / "state" / "handoff_planted.md"
            planted.parent.mkdir(parents=True)
            planted.write_text(raw, encoding="utf-8")
            _git(repo, "add", "state/handoff_planted.md")

            failed = _run([str(binary), *GITLEAKS_HOOK_ARGS], repo)
            self.assertNotEqual(failed.returncode, 0)
            _assert_values_hidden(failed, values)

            masked = mask(raw)
            planted.write_text(masked, encoding="utf-8")
            _git(repo, "add", "state/handoff_planted.md")
            passed = _run([str(binary), *GITLEAKS_HOOK_ARGS], repo)
            self.assertEqual(passed.returncode, 0)
            _assert_values_hidden(passed, values)

    def test_committed_fixture_is_allowlisted(self) -> None:
        text = GITLEAKS_TOML.read_text(encoding="utf-8")
        self.assertIn(r"^tests/fixtures/handoff_planted_secret\.md$", text)
        self.assertNotIn("'''tests/fixtures/'''", text)
        binary = _gitleaks_bin()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            _init_repo(repo)
            dest = repo / "tests" / "fixtures" / "handoff_planted_secret.md"
            dest.parent.mkdir(parents=True)
            shutil.copy(FIXTURE, dest)
            _git(repo, "add", "tests/fixtures/handoff_planted_secret.md")
            _git(
                repo,
                "-c",
                "user.email=privacy-hook-test@example.com",
                "-c",
                "user.name=privacy-hook-test",
                "commit",
                "-m",
                "fixture",
            )
            self.assertEqual(_gitleaks_findings(binary, repo), set())

    def test_bare_token_in_state_blocked_by_a_hook(self) -> None:
        binary = _gitleaks_bin()
        for token in (_synthetic_aws_access_key(), _synthetic_github_pat()):
            with tempfile.TemporaryDirectory() as tmp:
                repo = Path(tmp)
                _init_repo(repo)
                target = repo / "state" / "bare.md"
                target.parent.mkdir(parents=True)
                target.write_text(token + "\n", encoding="utf-8")
                self.assertIsNotNone(_mask_check_files().search("state/bare.md"))
                mask_proc = _run([*_mask_check_argv(), str(target)], ROOT)
                _git(repo, "add", "state/bare.md")
                leak_proc = _run([str(binary), *GITLEAKS_HOOK_ARGS], repo)
                _assert_values_hidden(mask_proc, [token])
                _assert_values_hidden(leak_proc, [token])
                self.assertTrue(mask_proc.returncode != 0 or leak_proc.returncode != 0)
                self.assertNotEqual(leak_proc.returncode, 0)

    def test_mask_check_blocks_pii_in_state_yaml_and_txt(self) -> None:
        files_re = _mask_check_files()
        matched = (
            "state/note.yaml",
            "state/note.txt",
            "state/NOTE.YAML",
            "state/NOTE.TXT",
            "state/nested/Foo.YML",
            "HANDOFF.md",
            "docs/HANDOFF.md",
            "handoffs/a.md",
            "handoffs/nested/a.yaml",
            "next_prompt.txt",
            "dir/next_prompt.md",
        )
        for rel in matched:
            self.assertIsNotNone(files_re.search(rel), rel)
        for rel in (
            "README.md",
            "docs/examples/HANDOFF_EXAMPLE_SYNTHETIC.md",
            "scripts/sanitize_input.py",
            "state/script.py",
        ):
            self.assertIsNone(files_re.search(rel), rel)

        email = _synthetic_email()
        ssn = _synthetic_ssn()
        body = f"email: {email}\nSSN: {ssn}\n"
        for rel in ("state/note.yaml", "state/note.txt"):
            with tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp) / rel
                target.parent.mkdir(parents=True)
                target.write_text(body, encoding="utf-8")
                failed = _run([*_mask_check_argv(), str(target)], ROOT)
                self.assertNotEqual(failed.returncode, 0, rel)
                self.assertIn("SECRETS DETECTED", failed.stderr)
                _assert_values_hidden(failed, [email, ssn])

    def _load_mask_check(self):
        path = ROOT / "scripts" / "mask_check.py"
        spec = importlib.util.spec_from_file_location("mask_check_hook", path)
        if spec is None or spec.loader is None:
            raise AssertionError("mask_check module missing")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_mask_check_hook_fails_closed_on_scp_pin(self) -> None:
        section = _mask_check_section()
        self.assertIn("language: python", section)
        self.assertNotIn("language: system", section)
        self.assertIn("git+https://github.com/ManintheCrowds/SCP.git@" + SCP_SHA, section)
        module = self._load_mask_check()
        self.assertEqual(module.PIN, SCP_SHA)
        self.assertTrue(module.pin_ok(module.installed_commit()))
        self.assertFalse(module.pin_ok(""))
        self.assertFalse(module.pin_ok("0" * 40))
        original = module.installed_commit
        module.installed_commit = lambda: "0" * 40
        try:
            self.assertEqual(module.main(), 1)
        finally:
            module.installed_commit = original

    def test_gitleaks_precommit_rev_is_commit_sha(self) -> None:
        text = _config_text()
        self.assertRegex(
            text,
            r"repo:\s*https://github.com/gitleaks/gitleaks\s+rev:\s*" + re.escape(GITLEAKS_COMMIT) + r"\b",
        )
        self.assertNotRegex(text, r"rev:\s*v8\.30\.1\b")
        version = _run([str(_gitleaks_bin()), "version"], ROOT)
        self.assertEqual(version.returncode, 0)
        self.assertIn(GITLEAKS_VERSION, version.stdout + version.stderr)

    def test_ci_runs_hook_tests_and_pinned_gitleaks(self) -> None:
        text = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("pip install -r requirements.txt", text)
        self.assertIn("python -m unittest tests.test_mask_check_hook", text)
        self.assertIn("repository: gitleaks/gitleaks", text)
        self.assertIn(f"ref: {GITLEAKS_COMMIT}", text)
        self.assertIn("detect --redact --config .gitleaks.toml", text)
        self.assertNotIn("gitleaks/gitleaks-action@", text)
        self.assertNotRegex(text, r"ref:\s*v?\d+\.\d+")

    def test_allowlist_blocks_lookalike_fixture_paths(self) -> None:
        token = _synthetic_aws_access_key()
        binary = _gitleaks_bin()
        relatives = (
            "state/tests/fixtures/leak.md",
            "docs/tests/fixtures/secret.md",
            "prefix_tests/fixtures/secret.md",
        )
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            _init_repo(repo)
            for rel in relatives:
                path = repo / rel
                path.parent.mkdir(parents=True)
                path.write_text(token + "\n", encoding="utf-8")
                _git(repo, "add", rel)
            _git(
                repo,
                "-c",
                "user.email=privacy-hook-test@example.com",
                "-c",
                "user.name=privacy-hook-test",
                "commit",
                "-m",
                "lookalikes",
            )
            found = _gitleaks_findings(binary, repo)
            for rel in relatives:
                self.assertIn(rel, found)
            report_text = "\n".join(sorted(found))
            self.assertNotIn(token, report_text)


if __name__ == "__main__":
    unittest.main()

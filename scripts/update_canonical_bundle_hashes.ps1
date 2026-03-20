# PURPOSE: Regenerate docs/canonical-bundle.sha256 for OpenHarness canonical bundle.
# Run from repo root or any cwd; script locates openharness root via its own path.

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$OutFile = Join-Path $RepoRoot "docs/canonical-bundle.sha256"

$fixed = @(
    ".cursor/commands/architect.md",
    ".cursor/commands/agent-native-audit.md",
    ".cursor/skills/tech-lead/SKILL.md",
    ".cursor/skills/secure-contain-protect/SKILL.md",
    ".cursor/skills/refactor-reuse/SKILL.md",
    ".cursor/docs/NOGIC_WORKFLOW.md",
    "docs/contracts/scp_mcp_v1.md",
    "docs/AGENT_NATIVE_CHECKLIST.md",
    "docs/CANONICAL_AGENT_BUNDLE.md",
    "docs/VERIFY_NOT_TRUST.md",
    "docs/MCP_TRANSPARENCY.md",
    "docs/MCP_PRIVATE_HOST.md",
    "docs/SCP_SERVER_RELEASES.md",
    "docs/THIRD_PARTY_NOTICES.md",
    "scripts/update_canonical_bundle_hashes.ps1",
    "scripts/verify_canonical_bundle.ps1"
)

$lines = New-Object System.Collections.Generic.List[string]

foreach ($rel in $fixed) {
    $full = Join-Path $RepoRoot ($rel -replace "/", [IO.Path]::DirectorySeparatorChar)
    if (-not (Test-Path -LiteralPath $full)) {
        Write-Error "Missing bundled file: $rel"
    }
    $hash = Get-FileHash -LiteralPath $full -Algorithm SHA256
    $lines.Add("$($hash.Hash.ToLowerInvariant())  $rel")
}

$anaDir = Join-Path $RepoRoot ".cursor/skills/agent-native-architecture"
if (-not (Test-Path -LiteralPath $anaDir)) {
    Write-Error "Missing agent-native-architecture skill directory"
}
Get-ChildItem -LiteralPath $anaDir -Recurse -File | Sort-Object FullName | ForEach-Object {
    $full = $_.FullName
    $rel = $full.Substring($RepoRoot.Path.Length).TrimStart("\", "/") -replace "\\", "/"
    $hash = Get-FileHash -LiteralPath $full -Algorithm SHA256
    $lines.Add("$($hash.Hash.ToLowerInvariant())  $rel")
}

$lines.Sort()
Set-Content -LiteralPath $OutFile -Value ($lines -join "`n") -NoNewline
Write-Host "Wrote $OutFile ($($lines.Count) entries)"

# PURPOSE: Verify OpenHarness canonical bundle files match docs/canonical-bundle.sha256.
param(
    [string]$RepoRoot = "",
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"
if (-not $RepoRoot) {
    $RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
}
$manifest = Join-Path $RepoRoot "docs/canonical-bundle.sha256"
if (-not (Test-Path -LiteralPath $manifest)) {
    Write-Error "Missing manifest: $manifest - run scripts/update_canonical_bundle_hashes.ps1"
}

$failed = $false
Get-Content -LiteralPath $manifest | ForEach-Object {
    $line = $_.Trim()
    if (-not $line) { return }
    if ($line -match '^([0-9a-fA-F]{64})\s+(.+)$') {
        $expected = $Matches[1].ToLowerInvariant()
        $rel = $Matches[2].Trim()
        $full = Join-Path $RepoRoot ($rel -replace "/", [IO.Path]::DirectorySeparatorChar)
        if (-not (Test-Path -LiteralPath $full)) {
            Write-Host "MISSING $rel"
            $failed = $true
            return
        }
        $hash = (Get-FileHash -LiteralPath $full -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($hash -ne $expected) {
            Write-Host "MISMATCH $rel"
            Write-Host "  expected $expected"
            Write-Host "  actual   $hash"
            $failed = $true
        } elseif (-not $Quiet) {
            Write-Host "OK $rel"
        }
    } else {
        Write-Error "Bad manifest line: $line"
    }
}

if ($failed) {
    exit 1
}
if (-not $Quiet) {
    Write-Host "verify_canonical_bundle: all entries match"
}
exit 0

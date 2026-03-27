# PURPOSE: Copy the standard "continue from handoff" prompt to clipboard.
# DEPENDENCIES: None.
# Integration: When copied to .cursor/scripts/, prompt path is scripts/../state/continue_prompt.txt.

param([switch]$Generate)

if ($Generate) {
    $genScript = Join-Path $PSScriptRoot 'generate_next_prompt.ps1'
    if (-not (Test-Path $genScript)) {
        Write-Error "generate_next_prompt.ps1 not found in scripts/. Remove -Generate or add that script."
        exit 1
    }
    & $genScript
    exit 0
}

$promptPath = Join-Path (Join-Path $PSScriptRoot '..') (Join-Path 'state' 'continue_prompt.txt')
$prompt = Get-Content -Path $promptPath -Raw
Set-Clipboard -Value $prompt
Write-Host "Copied. Open a new chat (Ctrl+L) and paste."

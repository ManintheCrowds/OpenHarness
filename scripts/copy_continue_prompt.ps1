# PURPOSE: Copy the standard "continue from handoff" prompt to clipboard.
# DEPENDENCIES: None.
# Integration: When copied to .cursor/scripts/, prompt path is scripts/../state/continue_prompt.txt.

param([switch]$Generate)

if ($Generate) {
    if (Test-Path (Join-Path $PSScriptRoot 'generate_next_prompt.ps1')) {
        & (Join-Path $PSScriptRoot 'generate_next_prompt.ps1')
        exit 0
    }
}

$promptPath = Join-Path (Join-Path $PSScriptRoot '..') (Join-Path 'state' 'continue_prompt.txt')
$prompt = Get-Content -Path $promptPath -Raw
Set-Clipboard -Value $prompt
Write-Host "Copied. Open a new chat (Ctrl+L) and paste."

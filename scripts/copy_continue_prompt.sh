#!/usr/bin/env bash
# PURPOSE: Copy the standard "continue from handoff" prompt to clipboard.
# DEPENDENCIES: pbcopy (macOS) or xclip/xsel (Linux).
# Integration: When copied to .cursor/scripts/, prompt path is scripts/../state/continue_prompt.txt.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROMPT_FILE="$SCRIPT_DIR/../state/continue_prompt.txt"
PROMPT=$(cat "$PROMPT_FILE")

if command -v pbcopy >/dev/null 2>&1; then
  printf '%s' "$PROMPT" | pbcopy
  echo "Copied. Open a new chat (Cmd+L) and paste."
elif command -v xclip >/dev/null 2>&1; then
  printf '%s' "$PROMPT" | xclip -selection clipboard
  echo "Copied. Open a new chat (Ctrl+L) and paste."
elif command -v xsel >/dev/null 2>&1; then
  printf '%s' "$PROMPT" | xsel --clipboard
  echo "Copied. Open a new chat (Ctrl+L) and paste."
else
  echo "No clipboard tool (pbcopy, xclip, xsel) found. Copy the following manually:"
  echo "---"
  printf '%s\n' "$PROMPT"
  echo "---"
fi

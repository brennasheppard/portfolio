#!/bin/bash
set -euo pipefail

# Only run in remote environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Static HTML/CSS/JS site — no dependencies to install.
# Install prettier for formatting/linting support.
if ! command -v prettier &>/dev/null; then
  npm install -g prettier --prefer-offline 2>/dev/null || npm install -g prettier
fi

echo "Session start hook complete."

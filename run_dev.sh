#!/usr/bin/env bash

# Color codes for printing
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RESET='\033[0m'

# Count lines of code, to make me feel good about myself
echo "\n${YELLOW}Counting lines of code ...${RESET}"
cloc . --exclude-dir=.venv

# Run app in dev mode
echo "\n${YELLOW}Running app in dev mode ...${RESET}"
uv run fastapi dev backend/server.py
echo "\n${YELLOW}Server stopped ${RESET}"
echo ""

# Run tests after app exit
echo "\n${YELLOW}Running tests ...${RESET}"
uv run pytest

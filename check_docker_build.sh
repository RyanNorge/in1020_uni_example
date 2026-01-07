#!/usr/bin/env bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RESET='\033[0m'

# Run normal pytest
echo "\n${YELLOW}Running local tests...${RESET}"
uv run pytest

# Make sure Docker Desktop is running
open -a Docker

# Build docker container
echo "\n${YELLOW}Building docker container...${RESET}"
set -e # exit on error
docker build -t bridge:test .
BUILD_EXIT_CODE=$?
if [ $BUILD_EXIT_CODE -ne 0 ]; then
    echo "${RED}Docker build failed with exit code $BUILD_EXIT_CODE${RESET}"
    exit $BUILD_EXIT_CODE
fi
echo "${GREEN}Docker build succeeded!${RESET}\n"
set +e # disable exit on error

# Run tests in docker container
echo "\n${YELLOW}Running tests in docker container...${RESET}"
docker run --rm bridge:test sh -c "uv run pytest -p no:cacheprovider"
TESTS_EXIT_CODE=$?
if [ $TESTS_EXIT_CODE -ne 0 ]; then
    echo "\n${RED}TESTS FAILED with exit code $TESTS_EXIT_CODE${RESET}\n"
    exit $TESTS_EXIT_CODE
fi
echo "\n${GREEN}Docker tests completed successfully!${RESET}\n"

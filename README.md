

# IN1020 Universet Example

A quick example app for the backend of UiO's IN1020 Universet project.

## Installing and running

This is a Python project using UV to manage the environment. If you do not have it installed you can find instructions [on their website](https://docs.astral.sh/uv/getting-started/installation/) or install it directly on a unix-like system with...
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


Run via the entrypoint with ...
```
sh main.sh
```

Run tests with ...
```
uv run pytest
```

## A bit about the project

No AI or code generation was used, just good ol' fashioned Google-ing, although I did copy/paste the Github Action test runner from another project.

Pytest is used for testing. The server endpoints are tested through a client over localhost, not just directly from code.

This has a protected main branch, so that a branch cannot be merged into main unless all tests are passed in Github Actions.


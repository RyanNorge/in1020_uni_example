

# IN1020 Universet Example

A simple and quickly built example app for the backend of UiO's IN1020 Universet project.

[👉 See it running in "production" here 👈](https://in1020.ryanburch.no)


## Installing and running

Here are the requirements to get this going on a Unix-like system. I have not tried the app on Windows.

This is a Python project using UV to manage the environment. If you do not have it installed you can find instructions [on their website](https://docs.astral.sh/uv/getting-started/installation/) or install it directly on a unix-like system with...
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


Run tests and app locally in dev mode with ...
```
sh run_dev.sh
```

Run just tests with ...
```
uv run pytest
```

Also, there is a script to test a docker build. You'll need the Docker CLI to run it. I suggest getting [Docker Desktop](https://www.docker.com/products/docker-desktop/) if you're on a Mac. It should be run from the root of the app.

## Cool Things I Did
- Continuous Integration and Deployment
- Github Action to run tests
- Protected main branch. Cannot be pushed unless tests pass.
- Running in Docker container on Digital Ocean App Platform
- DNS link to a subdomain
- Bash script to build local docker image, run tests within container, and delete image.
- Proper handling of environment variables.
- No AI code generation. No chatbot help, but I did read the AI summary thing when I Googled a couple of times.

## Tech Stack
- Python
- FastAPI
- UV
- Docker
- Github Actions

## A bit about the project

This is a super minimal implementation, all done quick and dirty. Just wanted to get something up fast to show for the IN1020 application, as I don't actually have any projects in a public repo. I'm sure I'll take this all down later.

No AI or code generation was used, just good ol' fashioned Google-ing.

I did reuse some code from another project for the Github Action, and the Docker build test script. The Dockerfile comes mostly from Astral, the makes of UV.

Pytest is used for testing. The server endpoints are tested through a client over localhost, not just directly from code.

This has a protected main branch, so that a branch cannot be merged into main unless all tests have already passed in Github Actions.

Spent about 4 hours total on it, give or take. About 2 hours on troubleshooting some problems with the deployment setup.

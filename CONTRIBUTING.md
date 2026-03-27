# Contributing

## Setup

```bash
git clone <repo-url>
cd sceptre-mcp-server
poetry install
```

## Running Tests

Run tests directly with pytest:

```bash
poetry run pytest -q
```

Run tests through [tox](https://tox.wiki/) for a specific Python version:

```bash
# Use the virtualenv tox binary directly (poetry run intercepts flags like -e)
$(poetry env info -p)/bin/tox -e py312
```

Run against all configured Python versions (3.10–3.13, skips missing interpreters):

```bash
$(poetry env info -p)/bin/tox
```

Run coverage check (fails under 90%):

```bash
$(poetry env info -p)/bin/tox -e coverage
```

Pass additional pytest arguments via `--`:

```bash
$(poetry env info -p)/bin/tox -e py312 -- -k "test_create_stack" -q
```

## Pre-commit Hooks

Install the pre-commit hooks (one-time setup):

```bash
pip install pre-commit
pre-commit install
```

Run all hooks manually against all files:

```bash
pre-commit run --all-files
```

Hooks run automatically on `git commit` and include flake8, black, yamllint, poetry-check, and tox (py312).

## Type Checking

```bash
poetry run mypy src/
```

## Project Specs

Design documentation lives in `.kiro/specs/sceptre-mcp-server/`:

- [Requirements](.kiro/specs/sceptre-mcp-server/requirements.md)
- [Design](.kiro/specs/sceptre-mcp-server/design.md)
- [Tasks](.kiro/specs/sceptre-mcp-server/tasks.md)

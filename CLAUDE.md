# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`squiral` — a pure-Python library + CLI (stdlib only, no runtime deps) that generates square spiral matrices. Source in `squiral/`, tests in `tests/`. Managed with Poetry.

Public API: `produce(size: int) -> list` (build matrix), `printout(s)` (render it), `main_cli(argv)` (CLI entry). Run the CLI as `poetry run squiral <size>` or `python -m squiral <size>`.

## Commands

- Install deps: `poetry install` (installs `pytest` + `pytest-cov` only — install `pre-commit` separately for black/flake8/mypy hooks).
- Test + coverage: `poetry run pytest --cov=squiral --cov-report term-missing tests/`
- Single test: `poetry run pytest -v tests/test_squiral.py::test_produce`
- Lint + format + types: `pre-commit run --all-files` (black, flake8 + bugbear, mypy, typos, add-trailing-comma).
- CI lint only: `flake8 . --select=E9,F63,F7,F82 --show-source` then `flake8 . --exit-zero` (CI pip-installs flake8 separately).

CI (`python-package.yml`) runs **flake8 + pytest only**. `/check` runs the fuller local gate (black → flake8 → mypy via pre-commit, then pytest).

## Style

- flake8: `max-line-length = 127`, `max-complexity = 10` (`.flake8`).
- mypy and full type hints are enforced via pre-commit — keep new code typed.
- Supported Python: 3.10–3.14. Don't use syntax newer than 3.10.

## Workflow

- Branch from `main` as `feature/<issue#>-slug` (e.g. `feature/165-add-3-13`).
- Conventional Commits for subjects (`feat:`, `fix:`, `chore:`).
- PR required — never push directly to `main`.
- Run `pre-commit run --all-files` and make it pass before opening a PR.

## Release (gotcha)

Publishing a **GitHub Release** (`python-publish.yml`, `on: release: published`) builds with Poetry and uploads to PyPI via `twine`. The token is the `PYPI_TOKEN` secret, passed as the `TWINE_PASSWORD` env var. A bare `git tag` push does NOT publish — only a published Release does. Only cut a Release when you intend to publish.

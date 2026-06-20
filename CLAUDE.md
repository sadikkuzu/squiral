# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`squiral` — a pure-Python library (stdlib only, no runtime deps) that generates square spiral matrices. Source in `squiral/`, tests in `tests/`. Managed with Poetry.

## Commands

- Install deps: `poetry install`
- Test + coverage: `poetry run pytest --cov=squiral --cov-report term-missing tests/`
- Single test: `poetry run pytest -v tests/test_squiral.py::test_produce`
- Lint (mirrors CI): `flake8 . --select=E9,F63,F7,F82 --show-source` then `flake8 . --exit-zero`
- All hooks at once: `pre-commit run --all-files` (black, flake8 + bugbear, mypy, typos, add-trailing-comma)

`/check` runs the full local gate (black → flake8 → mypy → pytest) in one step.

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

Tagging `vX.Y.Z` triggers a GitHub Actions workflow that builds with Poetry and publishes to PyPI (`twine`, `TWINE_PASSWORD` secret). Only tag a release when you intend to publish.

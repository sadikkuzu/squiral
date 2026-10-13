# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`squiral` — a pure-Python library + CLI (stdlib only, no runtime deps) that generates square spiral matrices. Source in `squiral/`, tests in `tests/`. Managed with [uv](https://docs.astral.sh/uv/) (`uv_build` backend, `uv.lock` committed).

Public API: `produce(size: int) -> list` (build matrix), `printout(s)` (render it), `main_cli(argv)` (CLI entry). Run the CLI as `uv run squiral <size>` or `python -m squiral <size>`.

## Commands

- Install deps: `uv sync` (creates `.venv/`, installs `pytest` + `pytest-cov` only — install `pre-commit` separately for black/flake8/mypy hooks).
- Test + coverage: `uv run pytest --cov=squiral --cov-report term-missing tests/`
- Single test: `uv run pytest -v tests/test_squiral.py::test_produce`
- Lint + format + types: `pre-commit run --all-files` (black, flake8 + bugbear, mypy, typos, add-trailing-comma).
- CI lint only: `uvx flake8 . --select=E9,F63,F7,F82 --show-source` then `uvx flake8 . --exit-zero` (flake8 is not a project dep; CI runs it via `uvx`).
- Build: `uv build` (wheel + sdist into `dist/`).

CI (`python-package.yml`) runs **flake8 + pytest only**. `/check` runs the fuller local gate (black → flake8 → mypy via pre-commit, then pytest).

## Style

- flake8: `max-line-length = 127`, `max-complexity = 10` (`.flake8`).
- mypy and full type hints are enforced via pre-commit — keep new code typed.
- Supported Python: 3.10–3.14. Don't use syntax newer than 3.10.

## Workflow

- Branch from `main` as `feature/<issue#>-slug` (e.g. `feature/165-add-3-13`).
- Conventional Commits for subjects (`feat:`, `fix:`, `chore:`).
- PR required — never push directly to `main`. Only exception: the release version-bump commit (see Release).
- Run `pre-commit run --all-files` and make it pass before opening a PR.

## Release (gotcha)

Publishing a **GitHub Release** (`python-publish.yml`, `on: release: published`) builds with `uv build` and uploads to PyPI via `uv publish`. The token is the `PYPI_TOKEN` secret, passed as the `UV_PUBLISH_TOKEN` env var. A bare `git tag` push does NOT publish — only a published Release does. Only cut a Release when you intend to publish.

Release steps (version bump goes straight to `main`, no PR):

1. On `main`, run `uv version X.Y.Z` — it bumps `version` in `pyproject.toml` and the project entry in `uv.lock`; commit only those two files. Commit with subject `vX.Y.Z` (e.g. `v0.6.0`) and push to `main`. `main` is protected (requires `pre-commit.ci - pr`), so this push uses the admin bypass.
2. Tag that commit `X.Y.Z` — no `v` prefix (e.g. `0.6.0`).
3. Publish a GitHub Release from that tag, titled `X.Y.Z`. This step uploads to PyPI.

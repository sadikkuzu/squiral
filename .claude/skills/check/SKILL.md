---
name: check
description: Run the local quality gate for the squiral repo — black, flake8, mypy (via pre-commit) plus pytest with coverage. Use before opening a PR or when the user asks to verify changes.
---

Run the local quality gate, in order. Stop at the first failure, report it, and offer to fix.

Note: black, flake8, and mypy are **pre-commit hooks**, not Poetry deps — `poetry run black/flake8/mypy` will fail in a clean `poetry install` env. Only `pytest`/`pytest-cov` are installed by Poetry. CI itself runs only flake8 + pytest; this gate is the fuller local check.

1. **Format + lint + types** — `pre-commit run --all-files`
   Covers black, flake8 (+ bugbear), mypy, and the other configured hooks in one pass.
2. **Tests + coverage** — `poetry run pytest --cov=squiral --cov-report term-missing tests/`

## Fallback when Poetry isn't on PATH

If `poetry` is missing or `poetry run pytest` fails, activate the project venv and run pytest from it (the runner lives there, not in the global env):

```bash
source ./venv/bin/activate && python -m pytest --cov=squiral --cov-report term-missing tests/
```

Report a concise pass/fail summary per step. On any failure, quote the exact error and propose the fix before editing.

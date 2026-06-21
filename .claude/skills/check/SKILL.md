---
name: check
description: Run the local quality gate for the squiral repo — black, flake8, mypy (via pre-commit) plus pytest with coverage. Use before opening a PR or when the user asks to verify changes.
---

Run the local quality gate, in order. Stop at the first failure, report it, and offer to fix.

Note: `pre-commit` (and black/flake8/mypy) are **pre-commit hooks**, not Poetry deps — `poetry run black/flake8/mypy` will fail in a clean `poetry install` env.
If `pre-commit` isn’t installed, install it first (e.g. `python -m pip install pre-commit` or `pipx install pre-commit`). Only `pytest`/`pytest-cov` are installed by Poetry. CI itself runs only flake8 + pytest; this gate is the fuller local check.

1. **Format + lint + types** — `pre-commit run --all-files`
   Covers black, flake8 (+ bugbear), mypy, and the other configured hooks in one pass.

## Fallback when Poetry isn't on PATH

If `poetry` is missing or `poetry run pytest` fails, create/activate a local venv and install the test deps, then run pytest:

```bash
# ensure virtualenv is installed
python -m pip show virtualenv >/dev/null 2>&1 || python -m pip install virtualenv
# create the venv/ dir only if it doesn't already exist
[ -d venv ] || virtualenv venv
source venv/bin/activate
python -m pip install "pytest>=8,<10" pytest-cov
python -m pytest --cov=squiral --cov-report term-missing tests/
```

Report a concise pass/fail summary per step. On any failure, quote the exact error and propose the fix before editing.

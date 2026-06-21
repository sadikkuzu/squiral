---
name: check
description: Run the local quality gate for the squiral repo — black, flake8, mypy (via pre-commit) plus pytest with coverage. Use before opening a PR or when the user asks to verify changes.
---

Run the local quality gate, in order. Stop at the first failure, report it, and offer to fix.

Note: black, flake8, and mypy run as **pre-commit hooks**. If the `pre-commit` runner isn't installed, install it first (`pipx install pre-commit` or `python -m pip install pre-commit`). pre-commit does NOT run the tests — step 2 runs pytest separately.

1. **Format + lint + types** — `pre-commit run --all-files`
   Covers black, flake8 (+ bugbear), mypy, and the other configured hooks in one pass.
2. **Tests + coverage** — run pytest in a local venv:
   ```bash
   # create the venv/ dir only if it doesn't already exist (stdlib venv)
   [ -d venv ] || python -m venv venv
   # activate (POSIX shells)
   source venv/bin/activate
   python -m pip install "pytest>=8,<10" pytest-cov
   python -m pytest --cov=squiral --cov-report term-missing tests/
   ```

Report a concise pass/fail summary per step. On any failure, quote the exact error and propose the fix before editing.

---
name: check
description: Run the full local quality gate for the squiral repo — black, flake8, mypy, and pytest with coverage, mirroring CI. Use before opening a PR or when the user asks to verify changes.
---

Run the same checks CI runs, in order. Stop at the first failure, report it, and offer to fix.

1. **Format** — `poetry run black squiral tests`
2. **Lint** — `poetry run flake8 . --select=E9,F63,F7,F82 --show-source` then `poetry run flake8 . --exit-zero`
3. **Types** — `poetry run mypy squiral`
4. **Tests + coverage** — `poetry run pytest --cov=squiral --cov-report term-missing tests/`

If `poetry run <tool>` fails because a tool isn't in the Poetry env, fall back to running the tool directly (it's installed via pre-commit), or run `pre-commit run --all-files` for steps 1–3.

Report a concise pass/fail summary per step. On any failure, quote the exact error and propose the fix before editing.

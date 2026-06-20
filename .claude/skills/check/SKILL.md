---
name: check
description: Run the full local quality gate for the squiral repo — black, flake8, mypy, and pytest with coverage, mirroring CI. Use before opening a PR or when the user asks to verify changes.
---

Run the same checks CI runs, in order. Stop at the first failure, report it, and offer to fix.

1. **Format** — `poetry run black squiral tests`
2. **Lint** — `poetry run flake8 . --select=E9,F63,F7,F82 --show-source` then `poetry run flake8 . --exit-zero`
3. **Types** — `poetry run mypy squiral`
4. **Tests + coverage** — `poetry run pytest --cov=squiral --cov-report term-missing tests/`

## Fallbacks when Poetry isn't on PATH

If `poetry` is missing or `poetry run <tool>` fails:

- **Steps 1–3 (black, flake8, mypy):** run `pre-commit run --all-files` — the hooks cover all three.
- **Step 4 (pytest):** activate the project venv first, then run pytest from it (the runner lives there, not in the Poetry/global env):
  ```bash
  source ./venv/bin/activate && python -m pytest --cov=squiral --cov-report term-missing tests/
  ```

Note: an `rtk` proxy may collapse pytest output to a bare `Pytest: No tests collected` line. That is filtered output, not the real result — re-run the exact command prefixed with `rtk proxy` (e.g. `rtk proxy python -m pytest ...`) to see the true pass/fail and coverage.

Report a concise pass/fail summary per step. On any failure, quote the exact error and propose the fix before editing.

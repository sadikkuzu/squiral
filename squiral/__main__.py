"""Squiral package main entry point.

This module allows the squiral package to be executed as a module
using 'python -m squiral'.
"""

from __future__ import annotations

from .main import main_cli


if __name__ == "__main__":
    raise SystemExit(main_cli())

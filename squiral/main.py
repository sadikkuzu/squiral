#!/usr/bin/env python3
"""CLI functions.

Author: SADIK KUZU (c) 2021-2022
"""
from __future__ import annotations

import argparse
import sys
from typing import Optional
from typing import Sequence

from squiral import printout
from squiral import produce


def main_cli(argv: Optional[Sequence[str]] = None) -> int:
    """Auxiliary function for CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="squiral size")
    args = parser.parse_args(argv)

    try:
        printout(produce(int(args.size)))
    except ValueError:
        print("Squiral size must be a positive integer!", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main_cli())

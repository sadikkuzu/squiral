#!/usr/bin/env python3
"""CLI functions for the squiral package.

This module provides command-line interface functionality for generating
and displaying square spirals.

Author: SADIK KUZU (c) 2021-2022
"""
from __future__ import annotations

import argparse
import sys
from typing import Optional
from typing import Sequence

from squiral import generate_squiral
from squiral import print_squiral


def main_cli(argv: Optional[Sequence[str]] = None) -> int:
    """Main CLI function for the squiral package.

    Args:
        argv: Command line arguments. If None, uses sys.argv.

    Returns:
        Exit code: 0 for success, 1 for error.
    """
    parser = argparse.ArgumentParser(
        description="Generate and display a square spiral of numbers",
    )
    parser.add_argument(
        "size",
        type=int,
        help="Size of the square spiral (positive integer)",
    )

    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        # argparse calls sys.exit on error, convert to return code
        return int(e.code) if e.code is not None else 1

    try:
        if args.size <= 0:
            raise ValueError("Size must be a positive integer")
        squiral = generate_squiral(args.size)
        print_squiral(squiral)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:  # pragma: no cover
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main_cli())

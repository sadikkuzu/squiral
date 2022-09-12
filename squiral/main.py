#!/usr/bin/env python3
"""CLI functions.

Author: SADIK KUZU (c) 2021-2022
"""
import sys

from squiral import printout
from squiral import produce


def main_cli():
    """Auxiliary function for CLI."""
    printout(produce(int(sys.argv[-1])))

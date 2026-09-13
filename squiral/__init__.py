"""Squiral package.

A Python package for generating and displaying square spirals.
"""

from .squiral import generate_squiral
from .squiral import get_next_direction
from .squiral import get_next_point
from .squiral import print_squiral
from .main import main_cli  # noreorder

# Backwards compatibility
produce = generate_squiral
printout = print_squiral
to_where = get_next_direction
next_point = get_next_point

__all__ = [
    "generate_squiral",
    "print_squiral",
    "get_next_direction",
    "get_next_point",
    "main_cli",
    # Backwards compatibility
    "produce",
    "printout",
    "to_where",
    "next_point",
]

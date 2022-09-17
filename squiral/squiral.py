#!/usr/bin/env python3
"""Main functions.

Author: SADIK KUZU (c) 2021-2022
"""
from __future__ import annotations

import argparse
from math import log10
from math import sqrt

_directions = [["up", "right"], ["down", "left"]]


def to_where(A: int) -> str:
    """Get the number in the squiral and return back to next direction as a return value.

    Args:
        A (int): the number in the squiral

    Returns:
        str: next direction: "up", "right", "down", "left"
    """
    if A == 1:
        return "right"
    initial = int(sqrt(A))
    initial2 = initial**2
    if A == initial2:
        return to_where(A - 1)
    middle = initial * (initial + 1)
    first = initial % 2
    second = 0 if A <= middle else 1
    return _directions[first][second]


def next_point(row: int, col: int, direction: str) -> tuple:
    """Return next point indices according to current indices and direction.

    Args:
        row (int): row index
        col (int): column index
        direction (str): next direction: "up", "right", "down", "left"

    Returns:
        tuple: next point indices
    """
    if direction == "right":
        col += 1
    elif direction == "left":
        col -= 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    return (row, col)


def produce(size: int) -> list:
    """Construct double array wrt square size.

    Args:
        size (int): square size

    Returns:
        list: squiral numbers in 2D array
    """
    if size < 1:
        return []
    s = [[0 for i in range(size)] for j in range(size)]
    r = c = (size - 1) // 2
    A = 1
    s[r][c] = A
    while size > 1:
        r, c = next_point(r, c, to_where(A))
        A += 1
        s[r][c] = A
        if A == size**2:
            return s
    return s


def printout(s: list):
    """Printout 2D array.

    Args:
        s (list): squiral numbers in 2D array
    """
    if s:
        R = C = len(s)
        RJ = int(log10(R * C)) + 1
        for r in range(R):
            for c in range(C):
                print(str(s[r][c]).rjust(RJ), end=" ")
            print()


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="squiral size")
    args = parser.parse_args()

    print("Welcome to Squiral!")
    print("Here is an example:")
    try:
        size = int(args.size)
    except Exception:
        size = 5
    printout(produce(size))

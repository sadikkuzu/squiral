#!/usr/bin/env python3
# SADIK KUZU (c) 2021

import sys
from math import sqrt, log10

directions = [["up", "right"], ["down", "left"]]


def to_where(A):  # here A is the number in the squiral
    if A == 1:
        return "right"
    initial = int(sqrt(A))
    initial2 = initial ** 2
    if A == initial2:
        return to_where(A-1)
    middle = initial * (initial+1)
    first = initial % 2
    second = 0 if A <= middle else 1
    return directions[first][second]  # and here is the next direction


def next_point(row, col, direction):
    if direction == "right":
        col += 1
    elif direction == "left":
        col -= 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    return (row, col)


def produce(size):
    if size < 1:
        return None
    s = [[0 for i in range(size)] for j in range(size)]
    r = c = (size-1) // 2
    A = 1
    s[r][c] = A
    while size > 1:
        r, c = next_point(r, c, to_where(A))
        A += 1
        s[r][c] = A
        if A == size**2:
            return s
    return s


def printout(s):  # pragma: no cover
    R = C = len(s)
    RJ = int(log10(R*C)) + 1
    for r in range(R):
        for c in range(C):
            print(str(s[r][c]).rjust(RJ), end=" ")
        print()


if __name__ == "__main__":  # pragma: no cover
    print("Welcome to Squiral!")
    print("Here is an example:")
    try:
        size = int(sys.argv[1])  # try: python3 squiral.py 7
    except Exception:
        size = 5
    printout(produce(size))

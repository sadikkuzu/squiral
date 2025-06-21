#!/usr/bin/env python3
"""Main functions for generating square spirals.

This module provides functions to generate and display square spirals,
where numbers are arranged in a spiral pattern starting from the center.

Author: SADIK KUZU (c) 2021-2022
"""
from __future__ import annotations

import argparse
from math import sqrt
from typing import List, Tuple

# Direction mappings for spiral generation
_DIRECTIONS = [["up", "right"], ["down", "left"]]


def get_next_direction(number: int) -> str:
    """Get the next direction for a given number in the spiral.

    Args:
        number: The current number in the spiral.

    Returns:
        The next direction: "up", "right", "down", or "left".

    Example:
        >>> get_next_direction(1)
        'right'
        >>> get_next_direction(2)
        'up'
    """
    if number == 1:
        return "right"

    initial = int(sqrt(number))
    initial_squared = initial**2

    if number == initial_squared:
        return get_next_direction(number - 1)

    middle = initial * (initial + 1)
    first_index = initial % 2
    second_index = 0 if number <= middle else 1

    return _DIRECTIONS[first_index][second_index]


def get_next_point(row: int, col: int, direction: str) -> Tuple[int, int]:
    """Calculate the next point coordinates based on current position and direction.

    Args:
        row: Current row index.
        col: Current column index.
        direction: Movement direction ("up", "right", "down", or "left").

    Returns:
        A tuple containing the next (row, col) coordinates.

    Raises:
        ValueError: If direction is not one of the valid directions.

    Example:
        >>> get_next_point(1, 1, "right")
        (1, 2)
        >>> get_next_point(1, 1, "up")
        (0, 1)
    """
    direction_map = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0),
    }

    if direction not in direction_map:
        raise ValueError(f"Invalid direction: {direction}")

    row_delta, col_delta = direction_map[direction]
    return (row + row_delta, col + col_delta)


def generate_squiral(size: int) -> List[List[int]]:
    """Generate a square spiral of the given size.

    Creates a 2D array where numbers are arranged in a spiral pattern
    starting from the center with 1 and spiraling outward.

    Args:
        size: The side length of the square spiral.

    Returns:
        A 2D list containing the spiral numbers.
        Returns empty list if size < 1.

    Example:
        >>> generate_squiral(3)
        [[7, 8, 9], [6, 1, 2], [5, 4, 3]]
    """
    if size < 1:
        return []

    # Initialize the grid with zeros
    spiral_grid = [[0 for _ in range(size)] for _ in range(size)]

    # Start from the center
    current_row = current_col = (size - 1) // 2
    current_number = 1
    spiral_grid[current_row][current_col] = current_number

    if size == 1:
        return spiral_grid

    # Generate the spiral
    while current_number < size**2:
        direction = get_next_direction(current_number)
        current_row, current_col = get_next_point(current_row, current_col, direction)
        current_number += 1
        spiral_grid[current_row][current_col] = current_number

    return spiral_grid


def print_squiral(spiral_grid: List[List[int]]) -> None:
    """Print the spiral grid in a formatted way.

    Args:
        spiral_grid: A 2D list containing the spiral numbers.

    Example:
        >>> grid = [[7, 8, 9], [6, 1, 2], [5, 4, 3]]
        >>> print_squiral(grid)
        7 8 9
        6 1 2
        5 4 3
    """
    if not spiral_grid:
        return

    rows = cols = len(spiral_grid)
    max_number = rows * cols
    field_width = len(str(max_number))

    for row in range(rows):
        for col in range(cols):
            print(str(spiral_grid[row][col]).rjust(field_width), end=" ")
        print()  # New line after each row


def main() -> None:
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Generate and display a square spiral of numbers",
    )
    parser.add_argument(
        "size",
        type=int,
        help="Size of the square spiral (positive integer)",
    )
    args = parser.parse_args()

    print("Welcome to Squiral!")
    print("Here is your spiral:")

    try:
        if args.size <= 0:
            raise ValueError("Size must be a positive integer")
        spiral = generate_squiral(args.size)
        print_squiral(spiral)
    except ValueError as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":  # pragma: no cover
    main()

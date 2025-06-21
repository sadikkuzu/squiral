from __future__ import annotations

import pytest

from squiral import generate_squiral
from squiral import print_squiral
from squiral.squiral import _DIRECTIONS
from squiral.squiral import get_next_direction
from squiral.squiral import get_next_point
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("number, direction", TestParams.data_to_where)
def test_get_next_direction(number, direction):
    """Test the get_next_direction function."""
    assert get_next_direction(number) == direction


@pytest.mark.parametrize(
    "row1, col1, direction, row2, col2",
    TestParams.data_next_point,
)
def test_get_next_point(row1, col1, direction, row2, col2):
    """Test the get_next_point function."""
    assert get_next_point(row1, col1, direction) == (row2, col2)


def test_get_next_point_invalid_direction():
    """Test get_next_point with invalid direction."""
    with pytest.raises(ValueError, match="Invalid direction"):
        get_next_point(0, 0, "invalid")


def test_directions_constant():
    """Test that the directions constant is properly defined."""
    assert _DIRECTIONS is not None
    assert len(_DIRECTIONS) == 2
    assert len(_DIRECTIONS[0]) == 2
    assert len(_DIRECTIONS[1]) == 2


@pytest.mark.parametrize(
    "size, output",
    TestParams.data_produce,
)
def test_generate_squiral(size, output):
    """Test the generate_squiral function."""
    assert generate_squiral(size) == output


def test_generate_squiral_edge_cases():
    """Test generate_squiral with edge cases."""
    assert generate_squiral(0) == []
    assert generate_squiral(-1) == []
    assert generate_squiral(1) == [[1]]


@pytest.mark.parametrize("size, output", TestParams.data_printout)
def test_print_squiral(capsys, size, output):
    """Test the print_squiral function."""
    print_squiral(generate_squiral(size))

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""


def test_print_squiral_empty():
    """Test print_squiral with empty grid."""
    print_squiral([])
    # Should not raise any exception

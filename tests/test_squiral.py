import pytest
from squiral import __version__, produce
from squiral.squiral import next_point, to_where, directions
from tests.testdata_squiral import data_to_where, data_next_point


def test_version():
    assert __version__ == '0.1.1'


@pytest.mark.parametrize("A, direction", data_to_where)
def test_yn(A, direction):
    assert to_where(A) == direction


@pytest.mark.parametrize("row1, col1, direction, row2, col2", data_next_point)
def test_ist(row1, col1, direction, row2, col2):
    assert next_point(row1, col1, direction) == (row2, col2)


def test_directions():
    assert directions is not None


def test_produce0():
    assert produce(0) is None


def test_produce1():
    assert produce(1) == [[1]]


def test_produce2():
    assert produce(2) == [[1, 2], [4, 3]]


def test_produce3():
    assert produce(3) == [[7, 8, 9], [6, 1, 2], [5, 4, 3]]

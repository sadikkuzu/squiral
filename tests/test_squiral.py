import pytest
from squiral import produce, printout
from squiral.squiral import next_point, to_where, directions
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("A, direction", TestParams.data_to_where)
def test_yn(A, direction):
    assert to_where(A) == direction


@pytest.mark.parametrize(
    "row1, col1, direction, row2, col2",
    TestParams.data_next_point,
)
def test_next_point(row1, col1, direction, row2, col2):
    assert next_point(row1, col1, direction) == (row2, col2)


def test_directions():
    assert directions is not None


@pytest.mark.parametrize(
    "size, output",
    TestParams.data_produce,
)
def test_produce(size, output):
    assert produce(size) == output


@pytest.mark.parametrize("size, output", TestParams.data_printout)
def test_printout(capsys, size, output):
    printout(produce(size))

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""

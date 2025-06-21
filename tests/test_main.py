from __future__ import annotations

import pytest

from squiral import main_cli
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("size, output", TestParams.data_printout)
def test_main_cli_success(capsys, size, output):
    """Test main_cli with valid input."""
    assert main_cli([str(size)]) == 0

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""


def test_main_cli_with_string_input(capsys):
    """Test main_cli with invalid string input."""
    assert main_cli(["aloha"]) == 1

    out, err = capsys.readouterr()
    assert out == ""
    assert "Error:" in err


def test_main_cli_with_negative_input(capsys):
    """Test main_cli with negative input."""
    assert main_cli(["-5"]) == 1

    out, err = capsys.readouterr()
    assert out == ""
    assert "Error:" in err


def test_main_cli_with_zero_input(capsys):
    """Test main_cli with zero input.""" 
    assert main_cli(["0"]) == 1

    out, err = capsys.readouterr()
    assert out == ""
    assert "Error:" in err

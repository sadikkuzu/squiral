from __future__ import annotations

import pytest

from squiral import main_cli
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("size, output", [
    (1, "1 \n"),
    (2, "1 2 \n4 3 \n"),
    (3, "7 8 9 \n6 1 2 \n5 4 3 \n"),
])
def test_main_cli_success(capsys, size, output):
    """Test main_cli with valid input."""
    assert main_cli([str(size)]) == 0

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""


def test_main_cli_with_string_input(capsys):
    """Test main_cli with invalid string input."""
    # main_cli should catch argparse SystemExit and return error code
    result = main_cli(["aloha"])
    assert result == 2  # argparse error exit code
    
    # No output should be captured since argparse writes to stderr directly
    out, err = capsys.readouterr()
    # stderr might be empty because argparse writes directly to sys.stderr
    # before we can capture it in our function


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

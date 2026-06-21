from __future__ import annotations

import subprocess
import sys

import pytest

from squiral import main_cli
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("size, output", TestParams.data_printout)
def test_main_cli(capsys, size, output):
    assert main_cli([str(size)]) == 0

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""


def test_main_cli_with_string_input(capsys):
    assert main_cli(["aloha"]) == 1

    out, err = capsys.readouterr()
    assert out == ""
    assert err == "Squiral size must be a positive integer!\n"


def test_python_m_squiral():
    """Guard `python -m squiral` entry point (squiral/__main__.py import)."""
    result = subprocess.run(
        [sys.executable, "-m", "squiral", "1"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "1 \n"
    assert result.stderr == ""

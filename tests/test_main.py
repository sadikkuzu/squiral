from __future__ import annotations

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

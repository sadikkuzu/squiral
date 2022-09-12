import sys
from unittest.mock import patch

import pytest

from squiral import main_cli
from tests.testdata_squiral import TestParams


@pytest.mark.parametrize("size, output", TestParams.data_printout)
def test_main_cli(capsys, size, output):
    with patch.object(sys, "argv", ["squiral", size]):
        main_cli()

    out, err = capsys.readouterr()
    assert out == output
    assert err == ""

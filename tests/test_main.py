def test_printout(mocker, capsys):
    mocker.patch("sys.argv", return_value=[1])
    from squiral import main_cli

    main_cli()

    out, err = capsys.readouterr()
    assert out == "1 \n"
    assert err == ""

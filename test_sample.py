from log_script import main


def test_truth():
    """Simple sanity check to ensure test suite runs."""
    assert True


def test_readme_mentions_project_name():
    with open("README.md", "r", encoding="utf-8") as handle:
        contents = handle.read()
    assert "TestCollegamento" in contents
    assert "TestDiCollegamento" in contents


def test_script_logs_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert "CIAO GABRIELE" in captured.out

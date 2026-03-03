from pathlib import Path

from pipeline_app.cli import main


def test_cli_generates_report(tmp_path: Path, monkeypatch) -> None:
    input_file = tmp_path / "input.md"
    output_file = tmp_path / "report.txt"
    input_file.write_text("alpha beta\ngamma\n", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        [
            "pipeline-cli",
            str(input_file),
            "--output",
            str(output_file),
        ],
    )

    main()

    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "Quality Pipeline Report" in content
    assert "TOTAL" in content


def test_cli_raises_for_missing_input(tmp_path: Path, monkeypatch) -> None:
    missing_file = tmp_path / "missing.md"
    output_file = tmp_path / "report.txt"

    monkeypatch.setattr(
        "sys.argv",
        [
            "pipeline-cli",
            str(missing_file),
            "--output",
            str(output_file),
        ],
    )

    try:
        main()
    except FileNotFoundError as exc:
        assert "Input file not found" in str(exc)
    else:
        raise AssertionError("Expected FileNotFoundError for missing input file")

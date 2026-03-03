from pathlib import Path

from pipeline_app.stats import build_report, compute_stats


def test_compute_stats(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.md"
    file_path.write_text("hello world\nthis is test\n", encoding="utf-8")

    result = compute_stats(file_path)

    assert result.file_name == "sample.md"
    assert result.lines == 2
    assert result.words == 5
    assert result.chars > 0


def test_build_report_contains_totals(tmp_path: Path) -> None:
    file_a = tmp_path / "a.md"
    file_b = tmp_path / "b.md"
    file_a.write_text("one two\n", encoding="utf-8")
    file_b.write_text("three four five\n", encoding="utf-8")

    report = build_report([file_a, file_b])

    assert "TOTAL" in report
    assert "a.md" in report
    assert "b.md" in report

def test_compute_stats_empty_file(tmp_path: Path) -> None:
    file_path = tmp_path / "empty.md"
    file_path.write_text("", encoding="utf-8")

    result = compute_stats(file_path)

    assert result.lines == 0
    assert result.words == 0
    assert result.chars == 0

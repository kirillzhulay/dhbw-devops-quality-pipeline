from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextStats:
    file_name: str
    lines: int
    words: int
    chars: int


def compute_stats(path: Path) -> TextStats:
    content = path.read_text(encoding="utf-8")
    lines = len(content.splitlines())
    words = len(content.split())
    chars = len(content)
    return TextStats(file_name=path.name, lines=lines, words=words, chars=chars)


def build_report(paths: list[Path]) -> str:
    stats = [compute_stats(path) for path in paths]
    total_lines = sum(item.lines for item in stats)
    total_words = sum(item.words for item in stats)
    total_chars = sum(item.chars for item in stats)

    report_lines = ["Quality Pipeline Report", "======================", ""]
    for item in stats:
        report_lines.append(
            f"{item.file_name}: lines={item.lines}, words={item.words}, chars={item.chars}"
        )

    report_lines.extend(
        [
            "",
            "TOTAL",
            f"lines={total_lines}, words={total_words}, chars={total_chars}",
        ]
    )
    return "\n".join(report_lines) + "\n"

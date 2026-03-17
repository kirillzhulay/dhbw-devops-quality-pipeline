from __future__ import annotations
import argparse
from pathlib import Path

from pipeline_app.stats import build_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate text statistics report.")
    parser.add_argument("inputs", nargs="+", help="Input text files")
    parser.add_argument("--output", required=True, help="Output report file")
    args = parser.parse_args()

    input_paths = [Path(p) for p in args.inputs]
    output_path = Path(args.output)

    for path in input_paths:
        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    report = build_report(input_paths)
    output_path.write_text(report, encoding="utf-8")
    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()

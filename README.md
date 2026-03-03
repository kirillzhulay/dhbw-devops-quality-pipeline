# dhbw-devops-quality-pipeline

End-to-End CI/CD Pipeline with focus on Quality.

## Local run
```bash
python -m pip install --upgrade pip
pip install -e .[dev]
ruff check .
black --check .
pytest -q
python -m pipeline_app.cli docs/input/chapter1.md docs/input/chapter2.md docs/input/chapter3.md --output build/report.txt
```

## CI steps
1. Quality checks (ruff, black)
2. Automated tests (pytest)
3. Build artifact (report + zip)

## Focus area
Quality: static checks + automated tests are mandatory gates before build.

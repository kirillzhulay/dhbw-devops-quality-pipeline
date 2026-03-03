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
2. Security checks: bandit, pip-audit
3. Automated tests (pytest). Tests include coverage reporting and fail below 85% coverage.
4. Build artifact (report + zip)
5. Deploy stage: The deploy stage transfers the build artifact into a target directory (deploy/target) to simulate automated deployment.

## Focus area
Quality: static checks + automated tests are mandatory gates before build.

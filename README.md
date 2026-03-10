# dhbw-devops-quality-pipeline

A small demo project for a **quality-oriented DevOps/CI/CD pipeline** using Python.
The focus is on reproducible local checks and clear Quality Gates (Linting, Format-Check, Tests) before a build artifact is generated.

## Project Goals

- Example of a simple, traceable Quality Pipeline
- Static code analysis and format checking as mandatory steps
- Automated tests as a Quality Gate
- Generation of a build artifact (text report)

## Schwerpunkt (Focus Area)
This project focuses on **Quality** (Automated Testing and Static Code Analysis) and **Security** (SAST). We demonstrate advanced depth through:
* **Quality Gates:** 85% mandatory test coverage and SonarCloud integration.
* **Security Auditing:** Automated vulnerability scanning using `bandit` and `pip-audit`.

## Technology Stack

- Python `>=3.11`
- Packaging/Build: `setuptools`, `wheel`
- Tests: `pytest`, `pytest-cov`
- Linting: `ruff`
- Formatting: `black`

## Project Structure

```text
.
├── docs/
│   └── input/
│       ├── chapter1.md
│       ├── chapter2.md
│       └── chapter3.md
├── src/
│   └── pipeline_app/
│       ├── __init__.py
│       ├── cli.py
│       └── stats.py
├── tests/
│   └── test_stats.py
├── build/
├── pyproject.toml
└── README.md
```

# Project Documentation

## Prerequisites
* **Python:** 3.11 or newer installed.
* **Recommended:** Use a virtual environment (`.venv`).

---

## Installation (local)
```bash
python -m pip install --upgrade pip
pip install -e .[dev]
```

## Running the Application

The CLI analyzes one or more text files to calculate specific metrics and writes the results directly into a report file.

### Metrics Collected
* **Number of lines**
* **Number of words**
* **Number of characters**

### Example Execution
```bash
python -m pipeline_app.cli \
  docs/input/chapter1.md \
  docs/input/chapter2.md \
  docs/input/chapter3.md \
  --output build/report.txt
```
After execution, the report is located under build/report.txt.

## Local Quality Checks
Before every commit, the following steps should be successful:

```bash
# Linting
ruff check .

# Format Check
black --check .

# Tests
pytest -q

# Optional with coverage
pytest --cov=src --cov-report=term-missing
```

### Pre-commit Automation
We use `pre-commit` to ensure code meets quality standards before it is even committed.
```bash
# Install the hooks
pre-commit install

# Run against all files manually
pre-commit run --all-files

## CI/CD Pipeline (Target Workflow)

Typical workflow in CI:

1.  **Install dependencies**
2.  **Linting** (`ruff check .`)
3.  **Format-Check** (`black --check .`)
4.  **Run tests** (`pytest -q`)
5.  **Generate report** (CLI)
6.  **Provide build artifact** (e.g., `build/report.txt` and optionally as a ZIP)

---

### SonarCloud Analysis
The pipeline integrates SonarCloud to provide deep static analysis, tracking:
* **Code Quality:** Automated detection of "code smells" and maintainability issues.
* **Technical Debt:** Estimation of the effort required to fix existing issues.
* **Security Hotspots:** Identification of potentially weak code patterns that require manual review.

### Quality Gates

* **Pipeline fails** if Linting fails
* **Pipeline fails** if Format-Check fails
* **Pipeline fails** if tests fail
* **Pipeline fails** if the SonarCloud Quality Gate status is "Failed"

The artifact is only generated or published once gates have passed.

## Test Coverage in the Project
The following core functions are currently tested:

* `compute_stats(...)` in `src/pipeline_app/stats.py`
* `build_report(...)` in `src/pipeline_app/stats.py`

The tests are located in `tests/test_stats.py`.

---

## Common Errors & Solutions

### **ModuleNotFoundError: No module named 'pipeline_app'**
* **Cause:** Package not installed (editable).
* **Solution:** `pip install -e .[dev]`

### **black --check . reports changes**
* **Cause:** Code does not match the formatter standard.
* **Solution:** `black .`

### **FileNotFoundError during CLI call**
* **Cause:** At least one input file does not exist.
* **Solution:**
    * Check paths
    * Ensure the files are present

## Development Notes
* Use the **Python version** according to `pyproject.toml`
* Always secure changes with `ruff`, `black --check`, and `pytest`
* Prefer **small, traceable commits**

---

## License
Currently, no license file is stored for this repository. If the project is to be published, a suitable `LICENSE` should be added.
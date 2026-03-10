# Decision Log - Architectural Decisions

This document justifies the technical choices made for this project.

## Tool Selection

* **GitHub Actions**: Selected as the CI/CD platform for its native integration with the repository and easy-to-use YAML configuration.
* **Python Mini-Project**: A Python-based CLI application was chosen to demonstrate CI concepts with minimal overhead and high readability.
* **ruff / black / pytest**: 
    * `pytest` provides a robust framework for functional testing with coverage integration.
    * `ruff` and `black` ensure a consistent code style and catch common programming errors early.
* **bandit / pip-audit**: These tools implement "Shift-Left Security" by identifying vulnerabilities in both the custom code and external dependencies during the CI phase.
* **pre-commit**: Selected to enforce a "Shift-Left" approach, catching formatting and linting issues locally before they reach the CI pipeline.
* **SonarCloud / SonarQube**: Chosen to provide a centralized dashboard for code quality, tracking technical debt and maintainability over time beyond simple test coverage.
* **Successful Build Criteria**: A build is considered successful only if it passes all linting checks, meets the 85% test coverage threshold, and identifies zero high-severity security vulnerabilities.

* **Successful Build Criteria:** A build is considered successful only if it passes all linting checks, meets the 85% test coverage threshold, and identifies zero high-severity security vulnerabilities.

## Deployment Strategy

* **Local Target Directory**: To keep the lab accessible and avoid external infrastructure costs, the deployment is simulated by moving the ZIP artifact to a specific folder using a bash script. This illustrates the logic of artifact delivery without requiring cloud credentials.

## Reference to the "Three Ways of DevOps"

1. **Flow**: Achieved through a clear, automated pipeline that moves code from commit to a deployable artifact without manual intervention.
2. **Feedback**: The pipeline provides rapid feedback (approx. 1-2 minutes) on code quality, security, and logic errors.
3. **Continuous Learning**: By documenting the architecture and decision-making process, the project remains reproducible and serves as a foundation for further improvements.

### Detailed Alignment with the "Three Ways"
1. **Flow**: Our automated pipeline moves code from commit to a deployable ZIP artifact without manual intervention, ensuring a smooth delivery lifecycle for our text/documentation files.
2. **Feedback**: Rapid feedback is provided locally via pre-commit (seconds) and in the cloud via GitHub Actions and SonarCloud (minutes). This tiered feedback loop ensures developers are notified of regressions at the earliest possible stage.
3. **Continuous Learning**: By documenting the architecture and automating quality control (formatting and linting), we create a reproducible foundation for further improvements and allow the team to focus on higher-level architectural robustness.
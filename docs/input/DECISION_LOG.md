# Decision Log - Architectural Decisions

This document justifies the technical choices made for this project.

## Tool Selection

* **GitHub Actions**: Selected as the CI/CD platform for its native integration with the repository and easy-to-use YAML configuration.
* **Python Mini-Project**: A Python-based CLI application was chosen to demonstrate CI concepts with minimal overhead and high readability.
* **ruff / black / pytest**: 
    * `pytest` provides a robust framework for functional testing with coverage integration.
    * `ruff` and `black` ensure a consistent code style and catch common programming errors early.
* **bandit / pip-audit**: These tools implement "Shift-Left Security" by identifying vulnerabilities in both the custom code and external dependencies during the CI phase.

## Deployment Strategy

* **Local Target Directory**: To keep the lab accessible and avoid external infrastructure costs, the deployment is simulated by moving the ZIP artifact to a specific folder using a bash script. This illustrates the logic of artifact delivery without requiring cloud credentials.

## Reference to the "Three Ways of DevOps"

1. **Flow**: Achieved through a clear, automated pipeline that moves code from commit to a deployable artifact without manual intervention.
2. **Feedback**: The pipeline provides rapid feedback (approx. 1-2 minutes) on code quality, security, and logic errors.
3. **Continuous Learning**: By documenting the architecture and decision-making process, the project remains reproducible and serves as a foundation for further improvements.
# Architecture Documentation

This document describes the data and pipeline flow of the DevOps quality-focused CI/CD pipeline.

## Pipeline Flow

The pipeline is implemented as a sequence of jobs with strict quality gates:

1. **Inputs**: Triggered by a code push or pull request to the `main` branch.
2. **Quality Checks**: Initial static analysis using `ruff` for linting and `black` for code formatting.
3. **Tests**: Automated unit tests using `pytest`. This stage includes coverage reporting and is configured to fail if coverage is below 85%.
4. **Security**: Security auditing of the source code using `bandit` and dependency scanning via `pip-audit`.
5. **Build Artifact**: Upon passing all previous gates, a text report is generated from the input documents using the `pipeline_app.cli` tool. The results, input files, and source code are then packaged into a ZIP archive.
6. **Deploy**: The artifact is transferred to a target directory (`deploy/target`) using a deployment script to simulate an automated rollout.

## Roles

* **Build Artifact**: Represents an immutable version of the verified code and generated reports. It ensures that exactly the version that passed the quality gates is moved toward deployment.
* **Deploy Target**: Simulates the production environment. The separation of build and deploy steps demonstrates a clear boundary between Continuous Integration and Continuous Deployment.
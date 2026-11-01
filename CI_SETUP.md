# Continuous Integration Setup Documentation

## Project Overview

This project implements a Student Management System developed in Python. To improve software quality and automate verification processes, a Continuous Integration (CI) pipeline was integrated using GitHub Actions.
The CI pipeline ensures that every code change is automatically checked through linting and automated testing before being accepted into the codebase.

## CI Tool Selected
GitHub Actions

GitHub Actions was selected because:
* Free for public repositories
* Integrated directly into GitHub
* Supports Python projects
* Easy workflow automation
* Supports test reports and artifacts

## CI Workflow
The workflow executes automatically whenever:
* Code is pushed to main branch
* Pull requests are created
* Existing pull requests are updated

Pipeline Stages:
1. Checkout Source Code
2. Setup Python Environment
3. Install Dependencies
4. Run Code Linting
5. Execute Unit Tests
6. Generate Test Report
7. Upload Test Report Artifact

## Linting
The pipeline uses:

flake8

Purpose:
* Enforce Python coding standards
* Detect syntax issues
* Improve code readability
* Prevent simple programming mistakes

## Testing Framework
The project uses:

pytest

The following test categories are executed:
* Unit Tests
* Integration Tests
* Validation Tests

## Test Reports

A JUnit-compatible XML report is generated:

test-report.xml

This report is automatically uploaded as a GitHub Actions artifact.

## Failure Handling
The pipeline is configured to fail when:
* Linting errors exist
* Unit tests fail
* Integration tests fail
* Dependencies cannot be installed

This prevents faulty code from being merged.

## Local Execution

Run linting:

flake8 .

Run tests:

pytest -v

Generate test report:

pytest --junitxml=test-report.xml

## Benefits of CI
The CI pipeline provides:
* Automated quality assurance
* Early bug detection
* Consistent test execution
* Improved maintainability
* Professional development workflow
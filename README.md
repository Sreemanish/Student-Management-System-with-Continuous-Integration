# Student Management System with Continuous Integration

## Project Overview
This project demonstrates the implementation of Continuous Integration (CI) practices in a Python application. The application is a Student Management System that manages student information, validates data, calculates average marks, and assigns grades. The project integrates automated testing, code quality analysis, and CI pipeline execution using GitHub Actions.

The primary objective of this project is to simulate a real-world software development workflow where every code change is automatically verified through testing and quality checks before being merged into the main branch.

## Objectives
* Develop a Python-based Student Management System.
* Implement automated unit and integration testing.
* Configure a Continuous Integration (CI) pipeline.
* Automate code quality checks using Flake8.
* Generate test reports automatically.
* Demonstrate CI/CD principles used in professional software development.

## Project Structure
student-management-system/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── exceptions.py
├── manager.py
├── run_demo.py
├── student.py
│
├── test_student.py
├── test_integration.py
│
├── requirements.txt
├── README.md
├── TESTING_GUIDE.md
└── CI_SETUP.md

## Features
### Student Management
* Create student records
* Store student details
* Calculate average marks
* Generate grades
* Manage multiple students

## Validation and Exception Handling
* Age validation
* Invalid data handling
* Custom exceptions

## Automated Testing
* Unit Testing using Pytest
* Integration Testing using Pytest
* Automated test execution

## Continuous Integration
* Automated workflow execution
* Code quality verification
* Test automation
* Test report generation

## Technologies Used
Technology	  Purpose
* Python 3.x	Application Development
* Pytest	Unit & Integration Testing
* Flake8	Code Quality Analysis
* Git	Version Control
* GitHub	Repository Hosting
* GitHub Actions	Continuous Integration

## Installation
### Clone Repository
git clone <repository-url>
cd student-management-system

## Install Dependencies
pip install -r requirements.txt

## Running the Application
python run_demo.py

## Running Unit Tests
pytest -v
Expected Result:

=====================
5 PASSED
=====================

## Running Code Quality Checks
flake8 .
This command checks the project for:

* Syntax issues
* Style violations
* Common coding mistakes

## Continuous Integration Setup
The CI pipeline is configured using GitHub Actions.

Workflow file:

.github/workflows/ci.yml
The workflow automatically executes whenever:

* Code is pushed to the repository
* A pull request is created
* Existing pull requests are updated

## CI Pipeline Stages
### 1. Checkout Repository
Downloads project files onto the runner.

### 2. Set Up Python Environment
Installs the specified Python version.

### 3. Install Dependencies
Installs all required packages from the project.

### 4. Run Linting
Executes Flake8 to verify code quality.

### 5. Run Tests
Executes all Pytest test cases.

### 6. Generate Test Report
Creates a JUnit XML report.

### 7. Upload Artifact
Stores the generated report for review.

## Test Cases Implemented
### Unit Tests
* test_student_creation
* test_average_marks
* test_grade
* test_invalid_age

## Integration Test
* test_complete_workflow

## CI Verification
The pipeline was tested by pushing updates to the GitHub repository.

Results:

✅ Dependencies Installed Successfully

✅ Linting Completed Successfully

✅ All Tests Passed

✅ Test Report Generated

✅ Workflow Completed Successfully

This confirms that the Continuous Integration pipeline is functioning correctly and automatically validates every code change.

## Benefits of Continuous Integration
* Early bug detection
* Improved code quality
* Automated verification
* Reduced manual testing effort
* Increased reliability
* Professional software development workflow

## Challenges Encountered
During implementation several issues were identified:

* Python import errors
* Git repository initialization issues
* YAML workflow configuration errors
* Flake8 style warnings
These issues were resolved through debugging, code correction, and workflow validation.

## Conclusion
This project successfully demonstrates the implementation of Continuous Integration in a Python environment. GitHub Actions automatically validates the quality of the application by performing linting, testing, and reporting tasks on every code update. The project highlights modern software engineering practices and showcases how automation can improve reliability, maintainability, and development efficiency.

## Author
### Sreemanish


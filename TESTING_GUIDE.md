# Testing Guide

## Project Name
### Student Management System with Continuous Integration

## 1. Overview
This document describes the testing strategy, test cases, execution procedures, and Continuous Integration validation process used in the Student Management System project.

The primary objective of testing is to ensure that all functionalities work as expected and that code changes do not introduce defects into the application.

Testing was automated using the Pytest framework and integrated into a GitHub Actions Continuous Integration (CI) pipeline.

## 2. Testing Environment
Component	Version
* Python	3.x
* Testing Framework	Pytest
* Linting Tool	Flake8
* CI Platform	GitHub Actions
* Operating System	Windows 11
* Version Control	Git & GitHub

## 3. Test Strategy
The project follows a layered testing approach:

### Unit Testing
Unit tests verify the functionality of individual methods and classes independently.

### Integration Testing
Integration tests verify interactions between different components of the application.

### Automated CI Testing
All tests are automatically executed whenever code is pushed to the repository.

## 4. Test Cases
## TC-01: Student Object Creation
### Objective
Verify that a student object can be created successfully.

### Test File
test_student.py

### Test Method
test_student_creation()

### Expected Result
Student object created successfully
Student data stored correctly

### Status
✅ Passed

## TC-02: Average Marks Calculation
### Objective
Verify correct average mark calculation.

### Test File
test_student.py

### Test Method
test_average_marks()

### Expected Result
Average marks should match expected calculation.

### Status
✅ Passed

## TC-03: Grade Assignment
### Objective
Verify grade generation based on average marks.

### Test File
test_student.py

### Test Method
test_grade()

### Expected Result
Correct grade should be assigned according to the student's average marks.

### Status
✅ Passed

## TC-04: Invalid Age Validation
### Objective
Ensure invalid student ages are rejected.

### Test File
test_student.py

### Test Method
test_invalid_age()

### Expected Result
Application should raise an exception for invalid age values.

### Status
✅ Passed

## TC-05: Complete Workflow Validation
### Objective
Validate interaction between Student and StudentManager classes.

### Test File
test_integration.py

### Test Method
test_complete_workflow()

### Expected Result
* Student objects created
* Students added to manager
* Records stored successfully
* Workflow completes without errors
Status
✅ Passed

## 5. Executing Tests Locally
### Run All Tests
Execute:

pytest -v
Example Output:

=========================
5 PASSED
=========================

## 6. Linting Validation
Code quality is verified using Flake8.

Run:

flake8 .
Purpose:

* Detect syntax issues
* Enforce coding standards
* Improve code readability
* Identify common programming mistakes

## 7. Continuous Integration Testing
The project uses GitHub Actions for automated testing.

Workflow Location:

.github/workflows/ci.yml
The pipeline automatically executes when:

* Code is pushed to the repository
* Pull requests are created
* Pull requests are updated

## 8. CI Pipeline Execution Flow
Developer Commit
        │
        ▼
GitHub Repository
        │
        ▼
GitHub Actions Trigger
        │
        ▼
Install Dependencies
        │
        ▼
Run Flake8 Linting
        │
        ▼
Execute Pytest Tests
        │
        ▼
Generate Test Report
        │
        ▼
Upload Test Artifact
        │
        ▼
Workflow Complete
## 9. Test Report Generation
The CI pipeline generates an XML test report:

test-report.xml
The report contains:

* Test execution results
* Pass/Fail status
* Execution details
* Summary statistics
The report is uploaded automatically as a GitHub Actions artifact.

## 10. CI Verification Evidence
To verify successful CI implementation:

1. A code change was committed to the repository.
2. The GitHub Actions workflow started automatically.
3. Dependencies were installed successfully.
4. Linting completed successfully.
5. All tests passed successfully.
6. Test report was generated and uploaded.

Verification Result:

✅ Workflow Triggered Successfully

✅ Dependencies Installed Successfully

✅ Linting Passed

✅ Tests Passed

✅ Test Report Generated

✅ Build Successful

## 11. Testing Summary
Category	Total	Passed	Failed
Unit Tests	4	4	0
Integration Tests	1	1	0
Total	5	5	0

## 12. Conclusion
The Student Management System was successfully tested using automated unit tests, integration tests, and continuous integration validation. All test cases passed successfully, confirming that the application functions correctly and meets the project requirements.

The integration of GitHub Actions ensures that every future code change is automatically validated before being merged, promoting high code quality, reliability, and adherence to modern software development practices.
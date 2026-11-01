import pytest
from student import Student


def test_student_creation():
    student = Student(
        1,
        "John",
        20,
        [80, 90]
    )

    assert student.name() == "John"


def test_average_marks():

    student = Student(
        1,
        "John",
        20,
        [80, 90, 100]
    )

    assert student.average_marks() == 90


def test_grade_a():
    student = Student(
        1,
        "John",
        20,
        [95, 90]
    )
    assert student.grade() == "A"


def test_invalid_age():

    with pytest.raises(ValueError):
        Student(
            1,
            "John",
            -5,
            [50]
        )

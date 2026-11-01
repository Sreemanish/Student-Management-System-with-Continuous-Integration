from student import Student
from manager import StudentManager


def test_complete_workflow():
    manager = StudentManager()
    student1 = Student(
        1,
        "John",
        20,
        [90, 95]
    )
    student2 = Student(
        2,
        "Alice",
        21,
        [80, 85]
    )

    manager.add_student(student1)
    manager.add_student(student2)

    assert len(manager.students) == 2

    assert manager.class_average() > 0

    top_student = manager.top_performer()

    assert top_student.name == "John"

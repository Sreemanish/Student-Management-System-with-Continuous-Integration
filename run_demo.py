from student import Student
from manager import StudentManager


def main():

    manager = StudentManager()

    student1 = Student(
        1,
        "John",
        20,
        [90, 85, 95]
    )

    student2 = Student(
        2,
        "Alice",
        21,
        [80, 88, 92]
    )

    manager.add_student(student1)
    manager.add_student(student2)

    print("Students Added Successfully")
    print()

    print("Class Average:")
    print(manager.class_average())
    print()

    print("Top Performer:")
    print(manager.top_performer().name)


if __name__ == "__main__":
    main()

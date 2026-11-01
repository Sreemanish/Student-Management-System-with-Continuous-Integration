class Student:
    def __init__(self, student_id, name, age, marks):
        if age <= 0:
            raise ValueError("Age must be positive")

        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average_marks()

        if avg >= 90:
            return "A"

        if avg >= 75:
            return "B"

        if avg >= 60:
            return "C"

        return "D"

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Invalid mark")

        self.marks.append(mark)

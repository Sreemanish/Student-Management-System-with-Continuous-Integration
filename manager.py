
class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):

        if student.student_id in self.students:
            raise ValueError("Duplicate ID")

        self.students[student.student_id] = student

    def get_student(self, student_id):

        if student_id not in self.students:
            raise KeyError("Student not found")

        return self.students[student_id]

    def remove_student(self, student_id):

        if student_id not in self.students:
            raise KeyError("Student not found")

        del self.students[student_id]

    def class_average(self):

        if not self.students:
            return 0

        averages = [
              student.average_marks()
              for student in self.students.values()
        ]

        return sum(averages) / len(averages)

    def top_performer(self):
        return max(
              self.students.values(),
              key=lambda s: s.average_marks()
            )

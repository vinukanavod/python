from Person import Person


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call Person's __init__
        self.student_id = student_id
        self.courses = {}
        self.gpa = 0.0

    def display_info(self):
        super().display_info()  # Call Person's display_info
        print(f"Student ID: {self.student_id}")
        print(self)

    def enroll_course(self, course_name):
        if course_name in self.courses:
            print(f"Already enrolled in {course_name}.")
        else:
            self.courses[course_name] = None  # No grade yet
            print(f"Enrolled in {course_name}.")

    def assign_grade(self, course_name, grade):
        """Simulates recording a grade (0.0 to 4.0 scale)."""
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade {grade} assigned for {course_name}.")
        else:
            print(f"Cannot assign grade. {course_name} not found.")
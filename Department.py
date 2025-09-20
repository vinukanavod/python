class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.faculty = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_student(self, student):
        self.students.append(student)
        student.department = self

    def info(self):
        print("department info:")
        print("departmant name :" , self.name)
        print("departmant courses :" , self.courses)
        print("departmant students :" , self.students)
        print("departmant faculty :" , self.faculty)

    def __str__(self):
        return f"{self.name} "

    def __repr__(self):
        return f"{self.name} "
from Person import Person


class Faculty(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id

    def display_info(self):
        super().display_info()
        print(f"Faculty ID: {self.faculty_id}")
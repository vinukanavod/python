# Person → Student, Faculty, Staff
# • Faculty → Professor, Lecturer, TA (Teaching Assistant)
# • Student → UndergraduateStudent, GraduateStudent
#
from Student import Student

student = Student("vinuka" , 23 , 3 )
student.display_info()
student.enroll_course("Maths")
student.enroll_course("Commerce")
student.enroll_course("Science")

print("list of cources :" , student.courses)
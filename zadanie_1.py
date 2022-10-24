from uczenie_maszynowe.klasy import Student

student1 = Student.Student('Julia', [100, 200, 300])
student2 = Student.Student('Jakub', [3, 4, 6])

print(student1.is_passed())
print(student2.is_passed())

class Student:
    
    class_year = 2023
    num_student = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 17)
student2 = Student("Patric", 20)

print(student1.name, student1.age, student1.class_year, student1.num_student )
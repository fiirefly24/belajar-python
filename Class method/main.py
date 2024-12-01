class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    # Instance method    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avgGpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"

student1 = Student("Shandy", 4)
student2 = Student("Square", 4)
student3 = Student("Pants", 4)
student4 = Student("Pat", 4)
        
print(f"{Student.get_count()} with average gpa is {Student.get_avgGpa()}")
# using oops to print data

class Student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks

    def details(self, student_label): 
        print(student_label) 
        print(f"Name: {self.name}") 
        print(f"Roll No: {self.rno}") 
        print(f"Marks: {self.marks}") 

student1 = Student("Rahul", 101, 85)
student2 = Student("Priya", 102, 92)

student1.details("Student 1:")
student2.details("Student 2:")
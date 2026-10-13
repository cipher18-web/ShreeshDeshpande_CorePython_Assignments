

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

    def display_details(self):
        print(f"""Name: {self.name}
Age: {self.age}
Roll Number: {self.roll}
Course: {self.course}""")

name = input("Enter Name: ")
age = input("Enter Age: ")
roll = input("Enter Roll Number: ")
course = input("Enter Course: ")

student_obj = Student(name, age, roll, course)
student_obj.display_details()

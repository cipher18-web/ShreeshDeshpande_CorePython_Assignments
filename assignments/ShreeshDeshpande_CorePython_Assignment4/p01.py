#creating a class

class student:

    def __init__(self,rno,name,col):
        self.name=name
        self.rno= rno
        self.col=col

    def showdata(self):
        print(f"rno={self.rno} name={self.name} per={self.col}")

name = input("Enter student name: ")
rno = input("Enter roll number: ")
col = input("Enter course: ")

s1=student(name,rno,col)
s1.showdata()
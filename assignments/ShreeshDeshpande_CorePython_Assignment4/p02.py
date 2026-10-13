#create a class and object

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name=name
        self.salary = salary
    
    def display_details(self):
        print(f"Employee ID: {self.emp_id}\nName: {self.name}\nSalary: {self.salary}")

emp_id = input("Enter Employee ID: ")
name = input("Enter Name: ")
salary = input("Enter Salary: ")


emp_obj = Employee(emp_id, name, salary)
emp_obj.display_details()
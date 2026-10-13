class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        print(f"""Name: {self.name}
Salary: {self.salary}
Department: {self.department}""")

name = input("Enter Name: ")
salary = input("Enter Salary: ")
department = input("Enter Department: ")

manager_obj = Manager(name, salary, department)
manager_obj.display_details()

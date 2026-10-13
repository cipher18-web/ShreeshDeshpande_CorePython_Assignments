class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = int(basic_salary)

    def calculate_hra(self):
        return int(self.basic_salary * 0.20)

    def calculate_da(self):
        return int(self.basic_salary * 0.10)

    def display_details(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        gross = self.basic_salary + hra + da
        print(f"""Employee: {self.name}
Basic Salary: {self.basic_salary}
HRA: {hra}
DA: {da}
Gross Salary: {gross}""")

name = input("Enter Name: ")
basic_salary = input("Enter Basic Salary: ")

emp_obj = Employee(name, basic_salary)
emp_obj.display_details()

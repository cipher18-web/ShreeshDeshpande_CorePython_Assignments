class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, per_hour, hours_worked):
        self.per_hour = per_hour
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.per_hour * self.hours_worked

ft_emp = FullTimeEmployee(40000)
pt_emp = PartTimeEmployee(200, 90) 

print(f"""Full-Time Employee Salary: ₹{ft_emp.calculate_salary()}
Part-Time Employee Salary: ₹{pt_emp.calculate_salary()}""")

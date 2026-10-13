#simple calculator using oops

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

calc=Calculator()
if op == "+":
    print (calc.add(num1, num2))
elif op == "-":
    print (calc.subtract(num1, num2))
elif op == "*":
    print (calc.multiply(num1, num2))
elif op == "/":
    print (calc.divide(num1, num2))
else:
    print ("Invalid operator")


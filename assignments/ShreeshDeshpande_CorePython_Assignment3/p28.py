#simple calculator using functions


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))


if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(subtract(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))
else:
    print("Invalid input. Please enter a valid operator.")
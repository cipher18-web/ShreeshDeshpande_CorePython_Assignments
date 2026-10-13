#creating a function to calculate areas of basic shapes

def circle(radius):
    return 3.14 * (radius ** 2)

def rectangle(length, width):
    return length * width

def square(side):
    return side ** 2

radius = float(input("Enter radius: "))
c_area = circle(radius)
print(f"Area of Circle = {c_area:.2f}\n")

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
rec_area = rectangle(length, width)
print(f"Area of Rectangle = {rec_area:.2f}\n")
    
side = float(input("Enter square side: "))
sq_area = square(side)
print(f"Area of Square = {sq_area:.2f}\n")
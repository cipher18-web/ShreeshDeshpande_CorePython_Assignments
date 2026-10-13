# calculating basic areas using oops

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

length = float(input("Enter length: "))
width = float(input("Enter width: "))

rect = Rectangle(length, width)

print(f"""Area: {rect.calculate_area()}
Perimeter: {rect.calculate_perimeter()}""")
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

circle_obj = Circle(5)
rectangle_obj = Rectangle(10, 5)
square_obj = Square(5)

print(f"""Circle Area: {circle_obj.area()}
Rectangle Area: {rectangle_obj.area()}
Square Area: {square_obj.area()}""")

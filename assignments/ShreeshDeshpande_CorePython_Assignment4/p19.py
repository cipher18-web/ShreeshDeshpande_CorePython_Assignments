class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * (self.radius ** 2), 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle_obj = Circle(5)
rectangle_obj = Rectangle(10, 5)

print(f"""Circle Area: {circle_obj.area()}
Rectangle Area: {rectangle_obj.area()}""")

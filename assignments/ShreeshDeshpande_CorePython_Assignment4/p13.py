class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def display_details(self):
        print(f"""Brand: {self.brand}
Speed: {self.speed} km/h
Doors: {self.doors}""")
--------------------------------------
brand = input("Enter Brand: ")
speed = input("Enter Speed: ")
doors = input("Enter Number of Doors: ")

car_obj = Car(brand, speed, doors)
car_obj.display_details()

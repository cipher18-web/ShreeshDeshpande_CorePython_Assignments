class Animal:
    def eat(self):
        print("Dog is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

dog_obj = Dog()
dog_obj.eat()
dog_obj.bark()

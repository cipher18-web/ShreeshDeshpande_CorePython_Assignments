class Animal:
    def sound(self):
        pass  

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog_obj = Dog()
cat_obj = Cat()

print(f"""Dog Sound: {dog_obj.sound()}
Cat Sound: {cat_obj.sound()}""")

#

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self): 
        total_price = self.price * self.quantity
        
        print(f"Product Name: {self.name}") 
        print(f"Price: {self.price}") 
        print(f"Quantity: {self.quantity}") 
        print(f"Total Price: {total_price}") 

product1 = Product("Laptop", 50000, 2)

product1.display()

class MobilePhone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = int(price)
        self.storage = storage

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price = int(self.price - discount_amount)

    def display_details(self, percentage):
        print(f"""Brand: {self.brand}
Model: {self.model}
Price: {self.price}
Storage: {self.storage}
Discount: {percentage}%
Final Price: {self.price}""")

brand = input("Enter Brand: ")
model = input("Enter Model: ")
price = input("Enter Price: ")
storage = input("Enter Storage: ")

phone_obj = MobilePhone(brand, model, price, storage)
phone_obj.apply_discount(10)
phone_obj.display_details(10)


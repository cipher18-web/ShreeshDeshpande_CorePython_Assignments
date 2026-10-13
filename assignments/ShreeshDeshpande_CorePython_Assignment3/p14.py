#updating a dictionary 

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
city = input("Enter city: ")
d = {"name": name,"age": age,"course": course,"city": city}

print(f"original age: {age}")

d[age]=int(input("updated age :"))

#creating a dictionary and print values through their keys

name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
city = input("Enter city: ")
d = {"name": name,"age": age,"course": course,"city": city}

print(f"name :{d["name"]}")
print(f"age: {d["age"]}")
print(f"course: {d["course"]}")
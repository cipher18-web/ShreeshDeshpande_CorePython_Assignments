#delete key value from dictionary

country=input ("enter your country: ")
name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
city = input("Enter city: ")
d = {"name": name,"age": age,"course": course,"city": city}

remove=input("enter key to remove: ")
d.pop(remove)
print(f"updated dictionary: {d}")
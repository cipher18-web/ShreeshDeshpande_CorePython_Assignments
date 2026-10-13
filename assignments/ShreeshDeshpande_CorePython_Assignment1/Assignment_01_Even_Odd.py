num= input("Enter a number: ")
if int(num) % 2 == 0:
    print(num, "is an even number.")
elif int(num) % 2 == 1:
    print(num, "is an odd number.")
else:
    print("Invalid input. Please enter a valid integer.")
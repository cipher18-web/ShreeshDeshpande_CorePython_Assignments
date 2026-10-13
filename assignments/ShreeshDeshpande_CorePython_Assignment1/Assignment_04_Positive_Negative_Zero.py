num=float(input("Enter a number: "))
if num>0:
    print(num, "is a positive number.")
elif num<0:
    print(num, "is a negative number.")
elif num==0:
    print(num, "is zero.")
else:
    print("Invalid input. Please enter a valid number.")
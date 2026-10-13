#creating a function to find a factorial

def fact(num):  
    res = 1
    for i in range(2, num + 1):
        res *= i
        
    return res
a=int(input("Enter number:"))
b=fact(a)
print(f"Factorial = {b}")

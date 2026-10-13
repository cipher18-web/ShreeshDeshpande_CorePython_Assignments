#check for a prime number using functions

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter number: "))
if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
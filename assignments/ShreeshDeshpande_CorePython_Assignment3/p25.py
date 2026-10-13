#create a fun() to check greatest number out of 3

def greatest(a, b, c):
    # print(f"Largest Number = {max(a, b, c)}")
     if a >= b and a >= c:
        return a
     elif b >= a and b >= c:
        return b
     else:
        return c
a, b, c = map(int, input("Enter numbers: ").split())

re=greatest(a, b, c)
print(f"Largest Number = {re}")
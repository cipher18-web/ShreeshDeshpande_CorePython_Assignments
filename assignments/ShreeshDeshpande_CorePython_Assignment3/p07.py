#searching for a number in set

a=set(map(int,input("set A :").split()))

if (b :=int(input("enter number to search: "))) in a :
    print(f"{b} is present in the set.")
else:
    print(f"{b} is not present in the set.")
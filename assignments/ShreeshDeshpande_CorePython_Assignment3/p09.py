#check for subset

a=set(map(int,input("set A :").split()))
b=set(map(int,input("set B :").split()))

if a^b:
    print("Set A is a subset of Set B.")
else:
    print("Set A is not a subset of Set B.")

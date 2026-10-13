#perfroming multiple set operations

a=set(map(int,input("set A :").split()))
b=set(map(int,input("set B :").split()))

print(f"union :{a|b}")
print(f"intersection :{a&b}")
print(f"A-B{a-b}")
print(f"Symmetric difference :{a^b}")

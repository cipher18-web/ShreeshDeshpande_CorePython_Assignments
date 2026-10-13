# adding and removing elements from a set

n=set()

element=map(int,input(f"original set: ").split())
n.update(element)
#add element
n.add(int(input("enter number to add: ")))
#remove element with no error
n.discard(int(input("enter number to remove: ")))

print(f"final set :{n}")
#store marks using dictionary

python=int(input ("python: "))
maths = int(input("maths: "))
database =int(input("database: "))
computernetworks= int(input("computer networks: "))
d = {"python": python,
     "maths": maths,
     "database": database,
     "computer networks": computernetworks
     }
print(f"total marks: {sum(d.values())}")

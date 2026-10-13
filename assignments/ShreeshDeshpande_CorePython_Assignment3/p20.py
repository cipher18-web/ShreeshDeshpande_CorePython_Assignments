#custom menu for dictionary functions

d={"name":"siri"}
print("""1.Add an item
2.Update an item
3.Delete an item
4.Search for an item
5.Display all items
6.Exit""")

num=input("Enter your choice:")

if num == '1': 
        
        key = input("Enter key: ")
        if key in d:
            print(f"Key '{key}' already exists!")
        else:
            value = input("Enter value: ").strip()
            d[key] = value
            print("Item added successfully.")
elif num == '2':
     
     k = input("Enter the key to update: ")
     if k in d:
            value = input("Enter new value: ").strip()
            d[k] = value
            print("Item updated successfully.")
     else:
            print(f"Key '{k}' not found in the dictionary.")
elif num == '3':
        
        key = input("Enter the key to delete: ").strip()
        if key in d:
            del d[key]
            print(f"Key '{key}' deleted successfully.")
        else:
            print(f"Key '{key}' not found.")
elif num == '4':

        key = input("Enter the key to search: ").strip()
        if key in d:
            print(f"Found! Key: {key} = Value: {d[key]}")
        else:
            print(f"Key '{key}' not found.")      
elif num == '5':

        if d:
            print("\nCurrent Dictionary Items ")
            for key, value in d.items():
                print(f"{key} : {value}")
        else:
            print("The dictionary is currently empty.")   
elif num == '6':
        # 6. Exit
        print("Exiting the program. Goodbye!")
        
else:
        print("Invalid choice! Please enter a number between 1 and 6.")
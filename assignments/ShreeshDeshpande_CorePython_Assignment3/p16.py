# Check whether a particular key exists in a dictionary

d = {"name":"virat" ,"age": 37,"course": "cricket","city": "delhi","country":"india"}

search=input("enter key to search: ")
if search in d:
    print(F"key '{search}' exists in dictionary")
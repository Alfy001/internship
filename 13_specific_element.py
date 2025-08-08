my_list = ['benz', 'bmw', 'audi', 'date']
to_find =input("Enter an element to find in the list: \n")
if to_find in my_list:
    print(f"'{to_find}' exists in the list.")
else:
    print("'{to_find}' does not exist in the list.")
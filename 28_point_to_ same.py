#28. Check if two variables point to the same object using is.
list_x = ['apple', 'banana']
list_y = list_x

if list_x is list_y:
    print("list_x and list_y reference the same memory location.")
else:
    print("list_x and list_y reference different memory locations.")

list_z = ['apple', 'banana']
if list_x is list_z:
    print("list_x and list_z reference the same memory location.")
else:
    print("list_x and list_z reference different memory locations.")

# This code checks if two variables point to the same object in memory.
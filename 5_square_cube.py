#find square and cube of a number
def square(n):
    return n*n
def cube(n):
    return n*n*n

n=int(input("enter the number: "))
switch = input("Enter \n's' for square or \n'c' for cube: \n")
if switch == 's':
    result = square(n)
    print(f"The square of {n} is: {result}")
elif switch == 'c':
    result = cube(n)
    print(f"The cube of {n} is: {result}")
else:
    print("Invalid input. Please enter 's' or 'c'.")

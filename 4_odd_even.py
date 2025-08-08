#check odd or even
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
result = check_odd_even(n)
print("The number is :", result)
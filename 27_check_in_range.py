#27 Check if a number is in a specific range (10 to 50).
def check_number_in_range(num):
    if 10 <= num <= 50:
        print(f"{num} is in the range of 10 to 50.")
    else:
        print(f"{num} is not in the range of 10 to 50.")

# Example usage:
number = int(input("Enter a number: "))
check_number_in_range(number)

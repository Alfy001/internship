#26. Check if a person is eligible to vote (age >= 18).
def check_vote_eligibility(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# Example usage:
age = int(input("Enter your age: "))
check_vote_eligibility(age)
#Write an expression using and and or to check multiple conditions.
def verify_entry(person_age, permission_granted, weekend_flag):
    if (person_age >= 18 and permission_granted) or weekend_flag:
        return "Access granted."
    else:
        return "Access denied."

# Example usage
print(verify_entry(20, True, False))   # Access granted
print(verify_entry(15, False, True))  # Access granted
print(verify_entry(16, False, False)) # Access denied

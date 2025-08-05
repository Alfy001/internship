def palindrome_check(s):
    return s == s[::-1]
s=input("enter the string :\n")
if palindrome_check(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
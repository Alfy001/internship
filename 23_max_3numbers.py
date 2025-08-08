def largest_of_three(x, y, z):
    return max(x, y, z)

val1 = int(input("Type the first value: "))
val2 = int(input("Type the second value: "))
val3 = int(input("Type the third value: "))

biggest_value = largest_of_three(val1, val2, val3)
print(f"The biggest number among the three is: {biggest_value}")

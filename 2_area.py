def calculate_area(radius):
    return 3.14 * radius * radius

r=int(input("enter the radius: "))
area = calculate_area(r)
print(f"The area of the circle is: {area}")
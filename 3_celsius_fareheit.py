#convert celsius to fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"The temperature in Fahrenheit is: ",f)

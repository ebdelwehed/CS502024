# Demonstrates rounding after the decimal point
x = float(input("Enter a number: "))
y = float(input("Enter a number: "))
z = round(x / y)
print(f"{x} divided by {y} is {z:.2f}")
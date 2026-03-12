# 6. Take three numbers and check if they are in geometric progression.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if b * b == a * c:
    print("The numbers are in Geometric Progression.")
else:
    print("The numbers are NOT in Geometric Progression.")

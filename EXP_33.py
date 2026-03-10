# 2. Take three numbers and check if they can form a Pythagorean triplet.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("These numbers form a Pythagorean Triplet")
else:
    print("These numbers do NOT form a Pythagorean Triplet")

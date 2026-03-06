# Q3. Take three numbers and print the median value (neither maximum nor minimum).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Median =", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Median =", b)
else:
    print("Median =", c)

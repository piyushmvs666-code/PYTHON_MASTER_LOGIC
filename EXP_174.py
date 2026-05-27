a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))

c = 180 - (a + b)

if a > 0 and b > 0 and c > 0:
    print("Third angle is:", c)
else:
    print("Invalid triangle angles.")

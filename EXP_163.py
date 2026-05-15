# 1. Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point lies at the Origin")
elif y == 0:
    print("Point lies on the X-axis")
elif x == 0:
    print("Point lies on the Y-axis")
else:
    print("Point does not lie on X-axis or Y-axis")

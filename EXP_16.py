x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("Point lies in First Quadrant.")
elif x < 0 and y > 0:
    print("Point lies in Second Quadrant.")
elif x < 0 and y < 0:
    print("Point lies in Third Quadrant.")
elif x > 0 and y < 0:
    print("Point lies in Fourth Quadrant.")
elif x == 0 and y == 0:
    print("Point lies at the Origin.")
elif x == 0:
    print("Point lies on Y-axis.")
else:
    print("Point lies on X-axis.")

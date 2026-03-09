# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.

day = int(input("Enter day number (1-7): "))

if day >= 1 and day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day number")

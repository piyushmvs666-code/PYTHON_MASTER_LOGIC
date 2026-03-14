#Take two dates (day and month) and determine which one comes first in the calendar.
day1 = int(input("Enter day of first date: "))
month1 = int(input("Enter month of first date: "))

# Input second date
day2 = int(input("Enter day of second date: "))
month2 = int(input("Enter month of second date: "))

# Compare dates
if month1 < month2:
    print("First date comes first in the calendar.")
elif month1 > month2:
    print("Second date comes first in the calendar.")
else:  # months are equal
    if day1 < day2:
        print("First date comes first in the calendar.")
    elif day1 > day2:
        print("Second date comes first in the calendar.")
    else:
        print("Both dates are the same.")

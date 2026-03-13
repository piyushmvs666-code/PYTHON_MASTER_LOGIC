# 3. Take day and month and check if it forms a valid calendar date (ignoring leap years).

day = int(input("Enter day: "))
month = int(input("Enter month: "))

if month == 2:
    if 1 <= day <= 28:
        print("Valid Date")
    else:
        print("Invalid Date")

elif month in [4, 6, 9, 11]:
    if 1 <= day <= 30:
        print("Valid Date")
    else:
        print("Invalid Date")

elif month in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= day <= 31:
        print("Valid Date")
    else:
        print("Invalid Date")

else:
    print("Invalid Month")

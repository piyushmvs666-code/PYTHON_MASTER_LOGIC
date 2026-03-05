n = int(input("Enter a 4-digit number: "))

if 1000 <= abs(n) <= 9999:
    first = n // 1000
    last = n % 10

    if first == last:
        print("First and last digits are equal.")
    else:
        print("First and last digits are not equal.")
else:
    print("Invalid input! Enter a 4-digit number.")

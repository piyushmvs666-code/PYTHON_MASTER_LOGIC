n = int(input("Enter a 3-digit number: "))

if 100 <= abs(n) <= 999:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if a != b and b != c and a != c:
        print("All digits are distinct.")
    else:
        print("Digits are not distinct.")
else:
    print("Invalid input! Please enter a 3-digit number.")

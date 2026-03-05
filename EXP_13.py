n = int(input("Enter a 3-digit number: "))

if 100 <= abs(n) <= 999:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    if b > a and b > c:
        print("Middle digit is the largest.")
    elif b < a and b < c:
        print("Middle digit is the smallest.")
    else:
        print("Middle digit is neither largest nor smallest.")
else:
    print("Invalid input!")

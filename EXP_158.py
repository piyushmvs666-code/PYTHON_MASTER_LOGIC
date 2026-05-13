n = int(input("Enter a number: "))

if n < 0:
    print("Negative numbers cannot be perfect squares.")
else:
    i = 0
    while i * i <= n:
        if i * i == n:
            print("Perfect square.")
            break
        i += 1
    else:
        print("Not a perfect square.")

# 7. Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.

n = int(input("Enter a 3-digit number: "))

first = n // 100
middle = (n // 10) % 10
last = n % 10

if first + last == middle:
    print("Sum of first and last digit equals the middle digit.")
else:
    print("Condition not satisfied.")

# 1. Count the number of digits in a given number
num = int(input("Enter a number: "))
temp = abs(num)  # handle negative numbers
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)

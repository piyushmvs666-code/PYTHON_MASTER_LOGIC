# Write a Python program to check whether a given number is an Armstrong number or not.
 num = int(input("Enter a number: "))

digits = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

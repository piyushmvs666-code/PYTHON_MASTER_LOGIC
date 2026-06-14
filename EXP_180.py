# Write a Python program to check whether a given number is a palindrome (a number that reads the same forwards
# and backwards).
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

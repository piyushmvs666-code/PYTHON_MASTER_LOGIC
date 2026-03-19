# 1. Print the product of digits of a given number
num = int(input("Enter a number: "))
product = 1

for digit in str(num):
    product *= int(digit)

print("Product of digits:", product)

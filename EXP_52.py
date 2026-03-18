# 3. Print the product of digits of a given number
num = int(input("\nEnter a number: "))
temp = abs(num)
product = 1

if temp == 0:
    product = 0
else:
    while temp > 0:
        digit = temp % 10
        product *= digit
        temp //= 10

print("Product of digits:", product)

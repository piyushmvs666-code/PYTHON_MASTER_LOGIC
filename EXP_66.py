# 7. Find the sum of all factors of a number.

num = int(input("Enter a number: "))
sum_of_factors = 0

for i in range(1, num + 1):
    if num % i == 0:
        sum_of_factors += i

print("Sum of factors is:", sum_of_factors)

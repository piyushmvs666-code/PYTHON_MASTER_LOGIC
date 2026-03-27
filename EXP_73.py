# Question: Find the sum of all factors of a number

num = int(input("Enter a number: "))
factor_sum = 0

for i in range(1, num + 1):
    if num % i == 0:
        factor_sum += i

print("Sum of all factors:", factor_sum)

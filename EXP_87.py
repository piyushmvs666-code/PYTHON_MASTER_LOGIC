# 8. Print factorial of each number from 1 to n

n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f"Factorial of {i} = {factorial}")

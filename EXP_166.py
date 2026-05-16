# 6. Print factorial of a number recursively.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number for factorial: "))
print("Factorial of", num, "is", factorial(num))

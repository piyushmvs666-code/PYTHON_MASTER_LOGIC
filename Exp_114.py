# 7. Calculate power of a number (xⁿ) using recursion.

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(base, "raised to the power", exponent, "is", power(base, exponent))

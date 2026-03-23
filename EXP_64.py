# 2. Find GCD (HCF) of two numbers using Euclid’s algorithm recursively
def gcd(a, b):
    # Base case
    if b == 0:
        return a
    # Recursive case
    return gcd(b, a % b)



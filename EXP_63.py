# 1. Find product of digits of a number recursively
def product_of_digits(n):
    # Base case: if number is 0, return 1 (neutral for multiplication)
    if n == 0:
        return 1
    # If single digit, return the digit itself
    if n < 10:
        return n
    # Recursive case
    return (n % 10) * product_of_digits(n // 10)

# Write a Python program to find the sum of digits of a number using recursion.

# Recursive function to find sum of digits
def sum_of_digits(n):
    # Base case: if number is 0
    if n == 0:
        return 0
    # Recursive case
    else:
        return (n % 10) + sum_of_digits(n // 10)

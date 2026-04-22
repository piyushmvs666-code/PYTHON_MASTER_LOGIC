 # Write a Python program to print the Fibonacci series up to n terms using recursion.

# Recursive function to return nth Fibonacci number
def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

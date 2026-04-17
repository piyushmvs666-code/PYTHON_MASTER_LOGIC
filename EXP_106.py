# Function to calculate sum of first n natural numbers using recursion
def sum_n(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: n + sum of (n-1)
    return n + sum_n(n - 1)

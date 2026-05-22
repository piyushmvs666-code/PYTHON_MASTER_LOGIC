# 1. Print sum of first n natural numbers recursively
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

# Example usage
n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is:", sum_n(n))

# 4. Print only odd numbers from 1 to n recursively

def print_odd(n):
    if n < 1:
        return
    print_odd(n - 1)
    if n % 2 != 0:
        print(n)

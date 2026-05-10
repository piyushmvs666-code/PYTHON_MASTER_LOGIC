# 1. Print numbers from 1 to n using recursion

def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)  # recursive call
    print(n)             # print after recursion

# 2. Print numbers from n down to 1 using recursion

def print_n_to_1(n):
    if n == 0:
        return
    print(n)             # print before recursion
    print_n_to_1(n - 1)  # recursive call

# Example
print("\nn to 1:")
print_n_to_1(5)

# 1. Print all numbers that are palindromes between 1–500

for num in range(1, 501):
    if str(num) == str(num)[::-1]:
        print(num)

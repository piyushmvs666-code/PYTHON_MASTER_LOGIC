# 3. Print numbers between 1–100 whose digits add up to a multiple of 3

print("\n\nNumbers whose digit sum is a multiple of 3 (1–100):")
for i in range(1, 101):
    digit_sum = sum(int(digit) for digit in str(i))
    if digit_sum % 3 == 0:
        print(i, end=" ")

# 2. Print all numbers that are palindromes between 1–500

print("\nPalindrome numbers between 1 and 500:")
for i in range(1, 501):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")

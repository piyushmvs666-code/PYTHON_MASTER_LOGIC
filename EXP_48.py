# Sum of all odd numbers up to n
n = int(input("Enter a number: "))
sum_odd = 0
for i in range(1, n + 1, 2):
    sum_odd += i

print("Sum of odd numbers:", sum_odd)

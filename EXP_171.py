# Sum of all even numbers up to n
n = int(input("Enter a number: "))
sum_even = 0
for i in range(2, n + 1, 2):
    sum_even += i
print("Sum of even numbers:", sum_even)

# 9. Print Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print(a)
else:
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

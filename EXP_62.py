# Q2. Print sum of first n terms of Fibonacci series.
n = int(input("Enter number of terms: "))
a, b = 0, 1
sum_fib = 0
for i in range(n):
    sum_fib += a
    a, b = b, a + b

print("Sum of first", n, "terms of Fibonacci series is:", sum_fib)

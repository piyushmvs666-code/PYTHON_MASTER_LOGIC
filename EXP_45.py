# Print the table of a given number (n × 1 to n × 10)
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

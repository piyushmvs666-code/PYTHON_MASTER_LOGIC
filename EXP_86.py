# 7. Print a pattern where each row i prints i*i

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i * i):
        print("*", end=" ")
    print()
  

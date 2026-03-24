# 3. Print all numbers between a and b divisible by 7

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print("Numbers divisible by 7 between", a, "and", b, "are:")

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)

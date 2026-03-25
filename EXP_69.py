# Print first n terms of a Geometric Progression
 = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter number of terms (n): "))

print("Geometric Progression:")
for i in range(n):
    term = a * (r ** i)
    print(term, end=" ")

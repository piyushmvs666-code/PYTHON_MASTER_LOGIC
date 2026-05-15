# Print first n terms of an Arithmetic Progression
a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))
print("Arithmetic Progression:")
for i in range(n):
    term = a + i * d
    print(term, end=" ")

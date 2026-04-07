num = input("Enter a number: ")

smallest = 9
largest = 0

for digit in num:
    d = int(digit)
    if d < smallest:
        smallest = d
    if d > largest:
        largest = d

print("Smallest digit:", smallest)
print("Largest digit:", largest)

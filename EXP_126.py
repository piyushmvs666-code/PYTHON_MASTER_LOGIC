# 10. Take 5 numbers as input. If the user enters 0, skip it using continue.
# At the end, print the sum of all non-zero numbers entered

total = 0

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    
    if num == 0:
        continue
    
    total += num

print("Sum of non-zero numbers:", total)

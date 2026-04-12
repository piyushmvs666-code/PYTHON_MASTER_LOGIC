# 1. Print all numbers from 1–n whose binary representation has an even number of 1s

n = int(input("Enter n: "))

print("Numbers with even number of 1s in binary:")
for i in range(1, n + 1):
    binary = bin(i)           # convert to binary
    count_ones = binary.count('1')
    
    if count_ones % 2 == 0:
        print(i, "->", binary)

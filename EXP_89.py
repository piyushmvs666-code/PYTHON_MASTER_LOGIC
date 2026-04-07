 6. Print all numbers from 1–n whose binary representation has an even number of 1s.

n = int(input("\nEnter value of n: "))

for i in range(1, n + 1):
    binary = bin(i)  # convert to binary
    ones_count = binary.count('1')
    
    if ones_count % 2 == 0:
        print(i, "->", binary)

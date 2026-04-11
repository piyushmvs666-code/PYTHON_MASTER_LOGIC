# Print all numbers whose sum of digits is even (1–100)

for num in range(1, 101):
    digit_sum = sum(int(digit) for digit in str(num))
    
    if digit_sum % 2 == 0:
        print(num, end=" ")

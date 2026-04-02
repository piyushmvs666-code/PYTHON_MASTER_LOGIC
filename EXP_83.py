# Program to print numbers between 1 and 100
# whose sum of digits is a multiple of 3

for num in range(1, 101): 
    digit_sum = sum(int(digit) for digit in str(num))  
    
    if digit_sum % 3 == 0:
        print(num) 

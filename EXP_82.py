# Program to print palindrome numbers between 1 and 500

for num in range(1, 501):  
    original = num
    reversed_num = int(str(num)[::-1])  
    
    if original == reversed_num:  
        print(num) 

# 2. Find sum of digits of a number recursively

def sum_of_digits(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)

number = int(input("\nEnter a number: "))
print("Sum of digits:", sum_of_digits(number))

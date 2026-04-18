# Write a Python function that finds the second largest number in a list without using built-in sorting.

💻 Solution:
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second


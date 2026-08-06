# Write a function that finds and returns the maximum number in a list without using Python's built-in max() function.
  pythondef find_maximum(numbers):
    # Return None if the list is empty
    if not numbers:
        return None
    
    # Assume the first number is the largest to start
    largest = numbers[0]
    
    # Compare with all other numbers in the list
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

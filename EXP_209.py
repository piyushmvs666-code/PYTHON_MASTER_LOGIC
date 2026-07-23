# Write a function that takes a list of numbers and returns the largest number without using Python's built-in max() function.
  def find_largest(numbers):
    if not numbers:
        return None  # Handle empty list case
    
    # Assume the first number is the largest to start
    largest = numbers[0]
    
    # Loop through the rest of the list
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

   

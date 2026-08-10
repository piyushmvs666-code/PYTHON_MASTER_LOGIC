# Write a Python function that extracts and returns all duplicate numbers from a list without modifying the original data.
  def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

# Take a list of items and return a new list containing only unique items.
  def remove_duplicates(items: list) -> list:
    # Sets inherently block duplicate entries
    return list(set(items))

numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]

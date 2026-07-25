# Find the Second Largest Number in a List.
  numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

numbers = list(set(numbers))  # Remove duplicate values

if len(numbers) < 2:
    print("Second largest number does not exist.")
else:
    numbers.sort()
    print("Second largest number is:", numbers[-2])

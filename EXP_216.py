# Write a Python program to find the second largest number in a list.
  numbers = [12, 45, 7, 89, 34, 89]

largest = second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print("Second largest number:", second)

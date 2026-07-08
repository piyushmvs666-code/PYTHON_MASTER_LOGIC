# Write a program that takes an integer input from the user and determines whether the number is even or odd.
  
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

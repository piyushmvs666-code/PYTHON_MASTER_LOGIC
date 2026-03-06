# Q1. Take a character and check if it is a letter, a digit, or neither.
ch = input("Enter a character: ")

if ch.isalpha():
    print("Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Neither letter nor digit")

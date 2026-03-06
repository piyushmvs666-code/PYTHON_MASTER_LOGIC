ch = input("Enter a character: ")

if ch.isalpha():
    print("Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Neither letter nor digit")

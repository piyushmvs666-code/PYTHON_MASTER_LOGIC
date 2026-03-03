ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
else:
    if ch >= 'A' and ch <= 'Z':
        print("Uppercase Letter")
    elif ch >= 'a' and ch <= 'z':
        print("Lowercase Letter")
    elif ch >= '0' and ch <= '9':
        print("Digit")
    else:
        print("Special Character")
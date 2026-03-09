# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit).

password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if len(password) >= 8 and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")

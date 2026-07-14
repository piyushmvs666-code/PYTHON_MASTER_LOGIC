# Check if a Single Character is a Vowel.
  
char = input("Enter a letter: ")
if char.isalpha() and len(char) == 1:
    # Convert to lowercase to handle both 'A' and 'a'
    if char.lower() in "aeiou":
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single letter.")

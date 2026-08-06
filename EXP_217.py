# Write a Python program that asks the user to input a single word. The program must then count how many vowels (a, e, i, o, u) are in that word and print the final count. The program should handle both uppercase and lowercase letters.
  def count_vowels(word):
    # Define a set of vowels for quick lookup
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    # Loop through each letter in the word
    for letter in word:
        if letter in vowels:
            vowel_count += 1
            
    return vowel_count

# --- Main Program Execution ---
# 1. Accept input from the user
user_word = input("Enter a word: ")

# 2. Call the function and get the total count
total_vowels = count_vowels(user_word)

# 3. Print the formatted result
print(f"The word '{user_word}' contains {total_vowels} vowels.")

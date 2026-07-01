#  Write a Python function that takes a string as input and returns a dictionary containing the frequency of each character in that string. The function should ignore spaces and be case-insensitive (e.g., 'A' and 'a' should be counted together)
   def count_char_frequencies(text):
    frequencies = {}
    cleaned_text = text.lower().replace(" ", "")
    for char in cleaned_text:
          frequencies[char] = frequencies.get(char, 0) + 1
         return frequencies

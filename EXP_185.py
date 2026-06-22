# *Question: Count frequency of each character in a string and return the most frequent one*
   def most_frequent_char(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]


#  Write a Python function that takes a string of text and returns a dictionary containing the count of each unique word. Ignore letter casing (e.g., "The" and "the" should be counted as the same word) and strip out common punctuation marks (., ,, !, ?).
   def count_word_frequencies(text):
    # Remove punctuation marks
    punctuation = ".,!?"
    for char in punctuation:
        text = text.replace(char, "")
    
    # Standardize casing and split into individual words
    words = text.lower().split()
    
    # Populate the frequency dictionary
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
            
    return frequency_dict

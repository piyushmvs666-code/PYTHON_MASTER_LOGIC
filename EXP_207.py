# Write a Python function that takes a string of text as input and returns a dictionary. The dictionary keys must be the unique words in lowercase, and the values must be the number of times each word appears. Ignore punctuation marks like periods and commas.
  def count_words(text):
    # Characters to remove from the text
    punctuation = ".,!?;:"
    
    # Remove punctuation marks
    for char in punctuation:
        text = text.replace(char, "")
        
    # Convert text to lowercase and split it into individual words
    words = text.lower().split()
    
    # Dictionary to hold our word counts
    word_counts = {}
    
    # Loop through each word and update its count
    for word in words:
        # .get(word, 0) returns the current count, or 0 if it is a new word
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

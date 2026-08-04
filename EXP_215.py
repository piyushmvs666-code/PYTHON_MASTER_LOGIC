# Find the Longest Word in a Text File.
  def find_longest_word(text):
    # Split text into a list of words
    words = text.split()
    
    if not words:
        return ""
    
    # Track the longest word
    longest = words[0]
    for word in words:
        # Strip punctuation if needed
        clean_word = word.strip(".,!?\"'")
        if len(clean_word) > len(longest):
            longest = clean_word
            
    return longest
  

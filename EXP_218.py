# Write a function count_words that takes a sentence and returns a dictionary showing how many times each word appears. Ignore punctuation and capitalization.
  def count_words(sentence):
    # Remove basic punctuation and lowercase the text
    for char in ".,!?":
        sentence = sentence.replace(char, "")
    
    words = sentence.lower().split()
    word_count = {}
    
    # Count occurrences
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    return word_count


# Given an input string, reverse the order of the words. The output should not contain leading, trailing, or multiple spaces between words.
  def reverse_words(text: str) -> str:
    # Split automatically handles multiple spaces and strips them
    words = text.split()
    # Reverse the list of words and join them with a single space
    return " ".join(reversed(words))


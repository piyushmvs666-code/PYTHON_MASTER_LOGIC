# Write a Python function that checks if a string is a palindrome. The function must ignore casing, spaces, and punctuation. It should return True if the clean string reads the same backward as forward, and False otherwise.
  def is_palindrome(text):
    """
    Checks if a string is a palindrome, ignoring non-alphanumeric characters.
    Uses the two-pointer technique for O(n) time and O(1) space efficiency.
    """
    # Initialize pointers at the beginning and end of the string
    left = 0
    right = len(text) - 1
    
    while left < right:
        # Move left pointer rightward if character is not a letter or number
        if not text[left].isalnum():
            left += 1
            continue
            
        # Move right pointer leftward if character is not a letter or number
        if not text[right].isalnum():
            right -= 1
            continue
            
        # Compare lowercase versions of the characters
        if text[left].lower() != text[right].lower():
            return False
            
        # Move both pointers inward if characters match
        left += 1
        right -= 1
        
    return True


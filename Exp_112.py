# Write a Python function that checks whether a given string is a palindrome (reads the same forward and backward), ignoring spaces and case.
def is_palindrome(text):
    # Normalize the string
    cleaned = text.replace(" ", "").lower()
    
    # Check if same forward and backward
    return cleaned == cleaned[::-1]

# Write a Python function to check if a string is a palindrome.
 def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    Ignores casing and spaces.
    """
    # Step 1: Clean the string (lowercase and remove spaces)
    cleaned_text = "".join(text.split()).lower()
    
    # Step 2: Compare the string with its reverse using slicing
    return cleaned_text == cleaned_text[::-1]

# --- Test Cases ---
if __name__ == "__main__":
    test_strings = ["radar", "Hello", "A man a plan a canal Panama", "racecar"]
    
    for string in test_strings:
        result = is_palindrome(string)
        print(f"Is '{string}' a palindrome? -> {result}")

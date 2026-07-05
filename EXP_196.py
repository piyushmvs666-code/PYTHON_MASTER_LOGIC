# The most efficient way to solve this is by using a Python dictionary to count occurrences, then scanning the string a second time.pythondef first_uniq_char(s: str) -> int:
    # Step 1: Build the character frequency count
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    # Step 2: Find the first character with a count of 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
            
    # Return -1 if no unique character exists
    return -1

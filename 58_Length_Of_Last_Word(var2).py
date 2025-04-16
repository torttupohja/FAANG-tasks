def lengthOfLastWord(s):
    length = 0
    i = len(s) - 1

    # Step 1: Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Step 2: Count characters in the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

"""
Time: O(n) – because .split() and .rstrip() each scan the string once
Space: O(n) – for the list of words (can be optimized)
"""

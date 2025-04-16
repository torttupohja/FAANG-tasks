def lengthOfLastWord(s):
    # Step 1: Remove any trailing spaces at the end
    s = s.rstrip()

    # Step 2: Split the string into words by spaces
    words = s.split()

    # Step 3: Return the length of the last word
    return len(words[-1])
  
"""
Time: O(n) – because .split() and .rstrip() each scan the string once
Space: O(n) – for the list of words (can be optimized)
"""

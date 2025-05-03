def isAnagram(s, t):
    # Quick check: if lengths differ, can't be anagrams
    if len(s) != len(t):
        return False

    # Use a dictionary to count character frequencies
    from collections import Counter
    s_count = Counter(s)
    t_count = Counter(t)

    # Compare both dictionaries
    return s_count == t_count

"""
Time: O(n) → where n is the length of the strings
Space: O(1) → since the alphabet size (lowercase English letters) is fixed
"""

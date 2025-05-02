def wordPattern(pattern, s):
    words = s.split()
    
    # Quick check: pattern length must match number of words
    if len(pattern) != len(words):
        return False

    # Dictionaries to store mappings
    char_to_word = {}
    word_to_char = {}

    for c, w in zip(pattern, words):
        # Check mapping from pattern → word
        if c in char_to_word:
            if char_to_word[c] != w:
                return False  # Inconsistent mapping
        else:
            char_to_word[c] = w

        # Check mapping from word → pattern
        if w in word_to_char:
            if word_to_char[w] != c:
                return False  # Inconsistent reverse mapping
        else:
            word_to_char[w] = c

    return True

"""
Time: O(n) — where n is the number of words
Space: O(n) — for the two dictionaries
"""

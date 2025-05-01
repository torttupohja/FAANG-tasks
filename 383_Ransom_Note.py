def canConstruct(ransomNote, magazine):
    # Create a dictionary to count letters in magazine
    from collections import Counter
    magazine_count = Counter(magazine)

    # Check if each letter in ransomNote can be fulfilled
    for char in ransomNote:
        if magazine_count[char] > 0:
            magazine_count[char] -= 1  # Use up one occurrence
        else:
            return False  # Not enough of this character

    return True  # All letters matched

"""
Time: O(m + n) → m = length of ransomNote, n = length of magazine
Space: O(1) → fixed alphabet size (only lowercase English letters)
"""

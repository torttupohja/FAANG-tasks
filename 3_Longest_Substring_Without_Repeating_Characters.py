def lengthOfLongestSubstring(s):
    char_index = {}    # Dictionary to store the last seen index of each character
    left = 0           # Left pointer of the window
    max_length = 0     # Result: maximum length found

    # Move right pointer across the string
    for right in range(len(s)):
        # If we see a repeating character inside the current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to one position right of the last occurrence
            left = char_index[s[right]] + 1

        # Update the last seen index of the current character
        char_index[s[right]] = right

        # Update the max_length
        max_length = max(max_length, right - left + 1)

    return max_length

"""
Time: O(n) — each character is processed once
Space: O(k) — where k is the character set size (at most 26 for lowercase letters, or 128 for ASCII)
"""

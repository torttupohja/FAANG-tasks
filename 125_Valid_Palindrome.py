def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to next alphanumeric char
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to previous alphanumeric char
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters in lowercase
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
"""
Time	O(n)
Space	O(1) (in-place, no extra data structures)
"""

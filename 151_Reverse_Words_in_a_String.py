def reverseWords(s):
    # Step 1: Split the string into a list of words
    # The split() function automatically ignores extra spaces
    words = s.split()

    # Step 2: Reverse the list of words
    reversed_words = words[::-1]

    # Step 3: Join the reversed words with a single space
    result = ' '.join(reversed_words)

    return result

"""
Time: O(n) — traverses the string once
Space: O(n) — for storing words in a list
"""

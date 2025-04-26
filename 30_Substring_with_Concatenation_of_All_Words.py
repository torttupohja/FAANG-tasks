def findSubstring(s, words):
    if not s or not words:
        return []

    word_length = len(words[0])    # Length of each word (all words are same length)
    num_words = len(words)         # Total number of words
    total_length = word_length * num_words  # Total length of concatenated string
    word_count = {}                # Dictionary to count words

    # Build the word frequency dictionary
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    result = []  # To store starting indices

    # We only need to check starting from 0 to word_length positions
    for i in range(word_length):
        left = i                   # Left pointer of the window
        right = i                  # Right pointer of the window
        current_count = {}          # Current window word frequency

        while right + word_length <= len(s):
            # Extract a word from the window
            word = s[right:right + word_length]
            right += word_length

            if word in word_count:
                # Count the word in current window
                current_count[word] = current_count.get(word, 0) + 1

                # If we have more than expected, shrink the window from the left
                while current_count[word] > word_count[word]:
                    left_word = s[left:left + word_length]
                    current_count[left_word] -= 1
                    left += word_length

                # If window size matches exactly, record the start index
                if right - left == total_length:
                    result.append(left)
            else:
                # If word not in word_count, reset everything
                current_count.clear()
                left = right

    return result

"""
Time: O(N * W)
where N = len(s), W = len(words)
(because for each possible start, we check at most all words)

Space: O(W * K)
where K = length of a word (for the current_count and word_count dictionaries)
"""

def fullJustify(words, maxWidth):
    res = []            # Final result list of lines
    line = []           # Current line's words
    num_of_letters = 0  # Total characters in current line (excluding spaces)

    i = 0
    while i < len(words):
        word = words[i]

        # Check if adding this word exceeds maxWidth (including spaces between words)
        if num_of_letters + len(line) + len(word) > maxWidth:
            # Calculate how many spaces we need
            spaces_to_add = maxWidth - num_of_letters
            if len(line) == 1:
                # If only one word, left-justify with spaces at the end
                res.append(line[0] + ' ' * spaces_to_add)
            else:
                # Distribute spaces evenly
                space_between_words = spaces_to_add // (len(line) - 1)
                extra_spaces = spaces_to_add % (len(line) - 1)

                # Build the justified line
                justified_line = ''
                for j in range(len(line)):
                    justified_line += line[j]
                    if j < len(line) - 1:
                        # Add one extra space to the left-most gaps
                        justified_line += ' ' * (space_between_words + (1 if j < extra_spaces else 0))
                res.append(justified_line)

            # Reset for the next line
            line = []
            num_of_letters = 0
        else:
            # Add word to current line
            line.append(word)
            num_of_letters += len(word)
            i += 1

    # Last line - left justified
    last_line = ' '.join(line)
    last_line += ' ' * (maxWidth - len(last_line))  # Pad right
    res.append(last_line)

    return res

"""
Time: O(n * k) where n = number of words, k = average word length
Space: O(n * maxWidth) for storing the result
"""

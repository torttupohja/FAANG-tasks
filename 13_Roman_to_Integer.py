def romanToInt(s):
    # Step 1: Create a map of single Roman numeral characters to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0           # Final integer result
    prev_value = 0      # Value of the previous character (from right to left)

    # Step 2: Iterate over the string from right to left
    for char in reversed(s):
        current_value = roman_map[char]

        # Step 3: If current value is smaller than the previous one, it's a subtractive case
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        # Update prev_value for the next iteration
        prev_value = current_value

    return total

"""
Time: O(n) — where n is the length of the string s
Space: O(1) — constant dictionary and variables
"""

def convert(s, numRows):
    # Special case: if only one row, return the original string
    if numRows == 1 or numRows >= len(s):
        return s

    # Step 1: Create a list to hold strings for each row
    rows = [''] * numRows

    # Step 2: Initialize current row and direction
    current_row = 0
    going_down = False  # Direction flag

    # Step 3: Traverse the string and place characters in the correct row
    for char in s:
        rows[current_row] += char  # Add char to the current row

        # If we’re at the top or bottom, reverse the direction
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        # Move up or down
        current_row += 1 if going_down else -1

    # Step 4: Combine all rows into a single string
    return ''.join(rows)


"""
Time: O(n) — Each character is visited once
Space: O(n) — We store each character once across the rows
"""

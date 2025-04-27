def spiralOrder(matrix):
    result = []  # List to store the spiral order

    if not matrix:
        return result

    # Define the boundaries
    top, bottom = 0, len(matrix) - 1        # Top and bottom rows
    left, right = 0, len(matrix[0]) - 1      # Left and right columns

    # Traverse until the boundaries cross
    while top <= bottom and left <= right:
        # Step 1: Traverse from Left to Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1  # Move the top boundary down

        # Step 2: Traverse from Top to Bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1  # Move the right boundary left

        # Step 3: Traverse from Right to Left (only if still valid)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1  # Move the bottom boundary up

        # Step 4: Traverse from Bottom to Top (only if still valid)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1  # Move the left boundary right

    return result

"""
Time: O(m * n) — Visit each element once
Space: O(1) — No extra space used (besides the result list)
"""

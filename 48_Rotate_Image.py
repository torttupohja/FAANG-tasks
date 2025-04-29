def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    # Swap matrix[i][j] with matrix[j][i]
    for i in range(n):
        for j in range(i + 1, n):  # Only upper triangle (j > i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

"""
Time: O(n²) — Traverse every element once
Space: O(1) — In-place, no extra space
"""

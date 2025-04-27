def isValidSudoku(board):
    # Use sets to track seen numbers in rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # 3x3 boxes

    # Traverse every cell in the 9x9 board
    for r in range(9):
        for c in range(9):
            num = board[r][c]

            # Ignore empty cells
            if num == '.':
                continue

            # Calculate box index
            box_index = (r // 3) * 3 + (c // 3)

            # Check if the number already exists in row, column, or box
            if (num in rows[r]) or (num in cols[c]) or (num in boxes[box_index]):
                return False

            # Otherwise, record the number in respective row, column, and box
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_index].add(num)

    # If no violations, the board is valid
    return True

"""
Time: O(81) = O(1) — because it's always a fixed 9×9 board
Space: O(81) — for the 3 arrays of sets
"""

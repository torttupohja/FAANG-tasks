def solve(board):
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    def dfs(r, c):
        # Stop if out of bounds or not an 'O'
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'E'  # Mark escape
        # Explore all 4 directions
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # Step 1: Mark border-connected 'O's
    for r in range(rows):
        dfs(r, 0)          # Left border
        dfs(r, cols - 1)   # Right border
    for c in range(cols):
        dfs(0, c)          # Top border
        dfs(rows - 1, c)   # Bottom border

    # Step 2: Flip surrounded 'O's to 'X', and escape-marked 'E' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'  # Surrounded region
            elif board[r][c] == 'E':

"""
Time Complexity: O(m * n)
Every cell is visited at most once.

Space Complexity:
Worst case O(m * n) for recursion stack (DFS).
You can reduce this to O(m + n) with BFS using a queue.
"""

def gameOfLife(board):
    m, n = len(board), len(board[0])

    # Helper to count live neighbors
    def count_live_neighbors(r, c):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (board[nr][nc] == 1 or board[nr][nc] == 2):
                live_neighbors += 1
        return live_neighbors

    # First pass: apply rules with encoded values
    for r in range(m):
        for c in range(n):
            live_neighbors = count_live_neighbors(r, c)

            if board[r][c] == 1:
                # Rule 1 or 3: live cell dies
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = 2  # Mark as live → dead
            else:
                # Rule 4: dead cell becomes live
                if live_neighbors == 3:
                    board[r][c] = 3  # Mark as dead → live

    # Second pass: finalize the board
    for r in range(m):
        for c in range(n):
            if board[r][c] == 2:
                board[r][c] = 0  # Live → dead
            elif board[r][c] == 3:
                board[r][c] = 1  # Dead → live

"""
Time: O(m * n) — visit each cell twice
Space: O(1) — in-place (no extra grid)
"""

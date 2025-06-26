from collections import deque

def snakesAndLadders(board):
    n = len(board)

    def get_coords(square):
        """Convert 1-based square number to (row, col) in the board."""
        row = n - 1 - (square - 1) // n
        col = (square - 1) % n
        if (n - 1 - row) % 2 == 1:
            col = n - 1 - col  # Reverse for zigzag rows
        return row, col

    visited = set()
    queue = deque([(1, 0)])  # (square number, move count)

    while queue:
        square, moves = queue.popleft()
        if square == n * n:
            return moves

        for i in range(1, 7):  # Dice roll: 1 to 6
            next_square = square + i
            if next_square > n * n:
                continue
            r, c = get_coords(next_square)
            if board[r][c] != -1:
                next_square = board[r][c]  # Follow snake/ladder only once
            if next_square not in visited:
                visited.add(next_square)
                queue.append((next_square, moves + 1))

    return -1  # Unreachable

"""
Time Complexity: O(n²)
We may visit every square once. Each has up to 6 edges (dice rolls).

Space Complexity: O(n²)
For visited set and queue.
"""

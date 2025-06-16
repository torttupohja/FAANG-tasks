def numIslands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Check boundaries or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Mark as visited
        grid[r][c] = '0'

        # Visit all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c)

    return island_count

"""
Time Complexity: O(m * n)
We visit each cell once.

Space Complexity:
O(m * n) in the worst case due to recursion stack if the island spans most of the grid.
In iterative/BFS version: also O(m * n) in worst case queue usage.
"""

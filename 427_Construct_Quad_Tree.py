# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def construct(grid):
    n = len(grid)

    def build(r0, c0, size):
        # Check if the sub-square is uniform
        first = grid[r0][c0]
        uniform = True
        for r in range(r0, r0 + size):
            if not uniform: break
            for c in range(c0, c0 + size):
                if grid[r][c] != first:
                    uniform = False
                    break

        if uniform:
            return Node(bool(first), True)

        half = size // 2
        tl = build(r0, c0, half)
        tr = build(r0, c0 + half, half)
        bl = build(r0 + half, c0, half)
        br = build(r0 + half, c0 + half, half)
        # val can be anything for internal nodes; use True
        return Node(True, False, tl, tr, bl, br)

    return build(0, 0, n)

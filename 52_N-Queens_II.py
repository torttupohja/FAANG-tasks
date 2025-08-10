def totalNQueens(n):
    cols = set()
    pos_diag = set()  # r + c
    neg_diag = set()  # r - c
    count = 0

    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            backtrack(r + 1)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)

    backtrack(0)
    return count

"""
Time Complexity: O(n!)
Space Complexity: O(n)
"""

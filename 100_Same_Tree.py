# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    # Base case: both nodes are None → trees are identical at this branch
    if not p and not q:
        return True

    # If only one is None or values differ → trees are not the same
    if not p or not q or p.val != q.val:
        return False

    # Recursively compare left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

"""
Time: O(n) — Visit each node once (where n is number of nodes)
Space:
O(h) recursion stack space (where h is the height of the tree)
Worst case O(n) if tree is a straight line
"""

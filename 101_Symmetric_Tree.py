# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    # Helper function to compare two subtrees
    def isMirror(t1, t2):
        # Both nodes are None → symmetric
        if not t1 and not t2:
            return True
        # One is None or values differ → not symmetric
        if not t1 or not t2 or t1.val != t2.val:
            return False
        # Check mirror symmetry: left with right, right with left
        return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    # Start with the root mirrored with itself
    return isMirror(root, root)

"""
Time: O(n) — Every node is visited once
Space: O(h) — Recursive stack, h = height of tree
"""

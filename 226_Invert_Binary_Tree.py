# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    # Base case: empty node
    if not root:
        return None

    # Recursively invert left and right subtrees
    left_inverted = invertTree(root.left)
    right_inverted = invertTree(root.right)

    # Swap the inverted subtrees
    root.left = right_inverted
    root.right = left_inverted

    return root

"""
Time: O(n) — Each node is visited once
Space:
O(h) recursion stack, where h is the height of the tree
Worst case: O(n) (unbalanced tree)
Best case: O(log n) (balanced tree)
"""

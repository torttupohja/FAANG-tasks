# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # Base case: if the tree is empty
    if not root:
        return 0

    # Recursively compute depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Depth of current node is 1 + max of left/right subtree depths
    return 1 + max(left_depth, right_depth)

"""
Time: O(n) — Visit each node once
Space:
- Worst case: O(n) for recursion stack (unbalanced tree)
- Best case: O(log n) if the tree is balanced
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def validate(node, min_val, max_val):
        if not node:
            return True

        # Node must be strictly between min and max
        if not (min_val < node.val < max_val):
            return False

        # Check left and right subtrees with updated bounds
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))
"""
Time Complexity: O(n)
Every node is visited once.

Space Complexity: O(h)
Due to recursion stack — h = height of tree.
O(log n) for balanced tree, O(n) for skewed tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    prev = None      # To track previous value in in-order traversal
    min_diff = float('inf')  # Start with maximum possible value

    def inorder(node):
        nonlocal prev, min_diff
        if not node:
            return

        # Traverse left subtree
        inorder(node.left)

        # Process current node
        if prev is not None:
            diff = abs(node.val - prev)
            min_diff = min(min_diff, diff)
        prev = node.val  # Update previous to current

        # Traverse right subtree
        inorder(node.right)

    inorder(root)
    return min_diff

"""
Time and Space Complexity:
Time Complexity: O(n)
We visit every node exactly once (in-order traversal).

Space Complexity:
Recursive stack: O(h), where h is the height of the tree (log n for balanced, up to n for skewed).
No additional data structures used besides a few variables.
"""

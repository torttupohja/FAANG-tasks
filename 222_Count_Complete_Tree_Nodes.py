class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root):
    """
    Counts the number of nodes in a complete binary tree using binary search.
    Runs in O((log n)^2) time.
    """

    # Helper to compute the tree height (leftmost path)
    def getLeftHeight(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    # Helper to compute the tree height (rightmost path)
    def getRightHeight(node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    # Main logic
    if not root:
        return 0

    left_height = getLeftHeight(root)
    right_height = getRightHeight(root)

    if left_height == right_height:
        # Tree is a perfect binary tree => number of nodes = 2^height - 1
        return (1 << left_height) - 1
    else:
        # Recurse into left and right subtrees
        return 1 + countNodes(root.left) + countNodes(root.right)

"""
🧠 How It Works:
For a complete binary tree, if the left height == right height, the tree is perfect and we can compute nodes directly as 2^h - 1.
If not, we recursively count the left and right subtrees.
This method avoids visiting all nodes, giving us better than O(n) performance.

⏱️ Time and Space Complexity:
Time Complexity: O((log n)²)
Because we calculate height (log n) and do this height calculation at each level (log n).
Space Complexity: O(log n) for recursion stack (tree height).
"""

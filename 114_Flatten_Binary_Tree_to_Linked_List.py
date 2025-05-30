class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def flatten(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    # Keeps track of previously visited node
    prev = None

    def helper(node):
        nonlocal prev
        if not node:
            return

        # Traverse right first
        helper(node.right)
        # Then left
        helper(node.left)

        # Modify the pointers
        node.right = prev
        node.left = None
        prev = node

    helper(root)

"""
Time: O(n) — we visit each node once.
Space: O(h) — recursion stack, where h is the height of the tree (O(log n) for balanced, O(n) worst case for skewed).
"""

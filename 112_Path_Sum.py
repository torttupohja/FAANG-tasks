class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

  def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    # Base case: if the root is None, no path exists
    if not root:
        return False

    # If it's a leaf node, check if the path sum matches targetSum
    if not root.left and not root.right:
        return root.val == targetSum

    # Recursively check left and right subtrees
    # Subtract current node's value from targetSum
    new_target = targetSum - root.val

    return hasPathSum(root.left, new_target) or hasPathSum(root.right, new_target)

"""
Time: O(n) — we may visit all nodes in the worst case.

Space:
O(h) — where h is the height of the tree due to recursion stack
O(log n) for balanced trees, O(n) for skewed ones
"""

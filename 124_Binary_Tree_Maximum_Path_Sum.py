class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf')  # Initialize the maximum path sum

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Recursively compute the max path sum for left and right subtrees
        # Ignore paths with negative sums (treat them as 0)
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        # Path through the current node including both children
        current_path_sum = node.val + left + right

        # Update the global max path sum if current path is greater
        max_sum = max(max_sum, current_path_sum)

        # Return max path sum **starting** from current node going down one side
        return node.val + max(left, right)

    dfs(root)
    return max_sum

"""
🧠 Explanation:
Goal: Track the maximum path sum, considering:
The path may go through the current node and both children.
But when returning to the parent, we only take one child path (left or right).
We use dfs() to:
Compute max path starting from a node and going down.
Update max_sum if a larger total is found.

⏱️ Time and Space Complexity:
Time Complexity: O(n) — where n is the number of nodes.
Space Complexity: O(h) — height of the tree (due to recursion).
O(log n) for balanced trees
O(n) for skewed trees
"""

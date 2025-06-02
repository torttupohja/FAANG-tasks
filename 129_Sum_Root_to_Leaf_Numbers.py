class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def sumNumbers(root: TreeNode) -> int:
    # Helper function to do DFS traversal
    def dfs(node, current_sum):
        if not node:
            return 0

        # Update the current number by appending this digit
        current_sum = current_sum * 10 + node.val

        # If it's a leaf node, return the current number
        if not node.left and not node.right:
            return current_sum

        # Recursively compute the sum for left and right subtrees
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)

"""
🧠 Explanation:
We traverse the tree in DFS fashion.
At each node, we multiply the current sum by 10 and add the node’s value.
When we reach a leaf node, we return the computed number.
We accumulate these numbers as we go back up the tree.

⏱️ Time and Space Complexity:
Time: O(n) — where n is the number of nodes (we visit each node once).
Space: O(h) — height of the recursion stack.
O(log n) for a balanced tree
O(n) for a skewed tree
"""

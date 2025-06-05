class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    """
    Find the lowest common ancestor (LCA) of nodes p and q in a binary tree.
    """
    # Base case: if root is None or matches p or q, return root
    if not root or root == p or root == q:
        return root

    # Recursively search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are non-null, current root is the LCA
    if left and right:
        return root

    # Otherwise, return whichever is non-null (either left or right)
    return left if left else right

"""
🧠 How It Works:
If the current node is either p or q, return it.
Recursively search left and right subtrees.
If both p and q are found in different subtrees, the current node is their LCA.
If only one is found (in either left or right), propagate it upward.

⏱️ Time and Space Complexity:
Time Complexity: O(n), where n is the number of nodes in the tree (since we visit each node once)
Space Complexity: O(h), where h is the height of the tree (due to recursion stack)
"""

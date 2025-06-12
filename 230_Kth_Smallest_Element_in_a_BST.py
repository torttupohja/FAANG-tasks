class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    count = 0        # To track how many nodes we've seen
    result = None    # To store the kth smallest value

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return

        # Traverse left subtree
        inorder(node.left)

        # Visit current node
        count += 1
        if count == k:
            result = node.val
            return

        # Traverse right subtree
        inorder(node.right)

    inorder(root)
    return result

"""
Time Complexity: O(H + k)
In the worst case, we may need to go down H levels and visit up to k nodes.
H = log n for balanced BST, H = n for skewed tree.

Space Complexity:
O(H) due to recursion stack (or iterative stack if you use that version).
"""

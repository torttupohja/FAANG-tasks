from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Map from value to its index in inorder for fast lookup
    inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
    
    # Initialize index pointer for preorder traversal
    preorder_index = 0

    def helper(left: int, right: int) -> Optional[TreeNode]:
        nonlocal preorder_index

        # If there are no elements to construct the tree
        if left > right:
            return None

        # Pick up preorder_index element as the root
        root_val = preorder[preorder_index]
        preorder_index += 1

        # Build the root node
        root = TreeNode(root_val)

        # Root splits inorder list into left and right subtrees
        index = inorder_index_map[root_val]

        # Build left and right subtree recursively
        root.left = helper(left, index - 1)
        root.right = helper(index + 1, right)

        return root

    return helper(0, len(inorder) - 1)

"""
Time Complexity: O(n)
Each node is visited once, and the index lookup is O(1) thanks to the hash map.
Space Complexity: O(n)
"""

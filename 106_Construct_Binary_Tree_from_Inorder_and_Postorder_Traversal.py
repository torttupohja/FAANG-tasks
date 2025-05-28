from typing import List, Optional

# TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    # Map from value to index in inorder for fast lookup
    inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

    # Start from the last index of postorder (root of the tree)
    post_idx = [len(postorder) - 1]

    def helper(left: int, right: int) -> Optional[TreeNode]:
        # If there is no element to construct the tree
        if left > right:
            return None

        # Pick current root from postorder
        root_val = postorder[post_idx[0]]
        post_idx[0] -= 1

        # Create the root node
        root = TreeNode(root_val)

        # Root splits inorder into left and right subtrees
        index = inorder_index_map[root_val]

        # IMPORTANT: build right subtree first because postorder is Left → Right → Root
        root.right = helper(index + 1, right)
        root.left = helper(left, index - 1)

        return root

    return helper(0, len(inorder) - 1)

"""
Time Complexity: O(n)
Each node is processed exactly once.

Space Complexity: O(n)
For the recursion stack and the hashmap (inorder_index_map).
"""

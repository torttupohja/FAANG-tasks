from typing import List, Optional

# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None  # base case: no elements

        mid = len(nums) // 2
        root = TreeNode(nums[mid])  # middle element is the root

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
"""
Time Complexity: O(n) — each element is visited once to create the node.

Space Complexity: O(log n) on average (due to recursion stack height in a balanced BST).
Worst case is O(n) if the call stack doesn't collapse early (e.g., skewed list slicing).
"""

class BSTIterator:
    def __init__(self, root):
        """
        Initialize the stack and push all the leftmost nodes starting from root.
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        """
        Helper function to push all the left children of a subtree to the stack.
        This ensures that the smallest elements are on top.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        Returns the next smallest element in the BST.
        Pops from stack and processes the right child (if any).
        """
        top_node = self.stack.pop()
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return top_node.val

    def hasNext(self):
        """
        Returns True if there are more elements to traverse.
        """
        return len(self.stack) > 0

"""
Time Complexity:
next() → Average O(1) amortized (each node is pushed and popped once)
hasNext() → O(1)

Space Complexity: O(h), where h is the height of the tree
Due to the stack storing up to h nodes at most
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    Returns a list of lists, where each sublist contains the node values at each level of the tree.
    """
    if not root:
        return []

    result = []
    queue = deque([root])  # Use a queue to perform BFS

    while queue:
        level_size = len(queue)
        level = []

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            # Enqueue children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)  # Add current level to result

    return result

"""
🧠 Explanation:
Use a queue (BFS) to visit nodes level by level.
For each level, determine its size and process that many nodes.
Add each node's value to the current level list.
Append children to the queue for processing the next level.

⏱ Time and Space Complexity:
Time Complexity: O(n), where n is the total number of nodes in the tree.
Space Complexity: O(w), where w is the maximum width (maximum number of nodes at any level).
"""

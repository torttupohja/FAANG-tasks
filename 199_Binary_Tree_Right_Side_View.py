from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    """
    Returns the values of nodes visible from the right side.
    """
    if not root:
        return []

    result = []
    queue = deque([root])  # Use BFS level-order traversal

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()

            # The rightmost node is the last node in this level
            if i == level_size - 1:
                result.append(node.val)

            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

"""
🧠 Explanation:
We perform Breadth-First Search (BFS) using a queue.
At each level of the tree:
Traverse all nodes in that level.
The last node visited in the level is the rightmost one — add it to the result.
Keep adding left and right children into the queue.

⏱ Time and Space Complexity:
Time Complexity: O(n) — Each node is visited once.

Space Complexity: O(w) — Where w is the max width of the tree (can be O(n) in worst case).
"""

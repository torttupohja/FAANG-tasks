from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    """
    Returns a list of averages of each level in the binary tree.
    """
    if not root:
        return []

    result = []
    queue = deque([root])  # Queue for level-order traversal

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val  # Sum values in the current level

            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate average for this level
        average = level_sum / level_size
        result.append(average)

    return result

"""
🧠 Explanation:
Perform level-order traversal (BFS) using a queue.
At each level:
Accumulate the sum of all node values.
Compute the average as level_sum / level_size.
Append the average to the result list.

⏱ Time and Space Complexity:
Time Complexity: O(n), where n is the total number of nodes.
Space Complexity: O(w), where w is the maximum width of the tree (number of nodes at the widest level).
"""

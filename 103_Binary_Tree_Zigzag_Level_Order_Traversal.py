from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True  # This flag controls zigzag direction

    while queue:
        level_size = len(queue)
        level_nodes = deque()  # Use deque to efficiently append/pop from both ends

        for _ in range(level_size):
            node = queue.popleft()

            # Add the node value in the correct order
            if left_to_right:
                level_nodes.append(node.val)
            else:
                level_nodes.appendleft(node.val)  # Reverses order for this level

            # Enqueue children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(level_nodes))  # Convert deque to list before appending
        left_to_right = not left_to_right  # Flip direction for next level

    return result

"""
Time and Space Complexity:
Time Complexity: O(n)
Every node is visited once.

Space Complexity: O(n)
In the worst case, the queue and level storage can hold up to n nodes (for a wide level at the bottom).
"""

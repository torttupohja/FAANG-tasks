from collections import deque

def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    # Use a queue for BFS traversal
    queue = deque([root])

    while queue:
        level_size = len(queue)
        prev_node = None

        # Traverse current level
        for _ in range(level_size):
            node = queue.popleft()

            # Link previous node to current
            if prev_node:
                prev_node.next = node
            prev_node = node

            # Add child nodes to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Last node in the level should point to None (already is by default)

    return root

"""
Time: O(n) — each node is visited once.

Space: O(w) — where w is the maximum width of the tree (space used by queue). Worst case O(n).
"""

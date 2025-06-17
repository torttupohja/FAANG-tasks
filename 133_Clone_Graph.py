class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None

    old_to_new = {}  # Maps original node -> cloned node

    def dfs(curr):
        if curr in old_to_new:
            return old_to_new[curr]

        # Clone current node
        copy = Node(curr.val)
        old_to_new[curr] = copy

        # Recursively clone neighbors
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)

"""
Time Complexity: O(N + E)
N: number of nodes
E: number of edges
Each node and each edge is visited once.

Space Complexity: O(N)
Due to the recursion stack and the hash map for visited nodes.
"""

class Solution(object):
    def copyRandomList(self, head):
        visited = {}
        def copy(node):
            if not node:
                return node
            elif node in visited:
                return visited[node]
            new = Node(node.val)
            visited[node] = new
            new.next = copy(node.next)
            new.random = copy(node.random)
            return new
        return copy(head)
"""
Time complexity: O(n)
Space complexity: O(n)
"""

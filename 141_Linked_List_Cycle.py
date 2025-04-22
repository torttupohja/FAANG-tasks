class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # cycle detected

        return False  # reached the end, no cycle

"""
Time complexity is O(n) — where n is the number of nodes (worst case: traverse all nodes once).
Space complexity is O(1) — constant space, no extra structures.
"""

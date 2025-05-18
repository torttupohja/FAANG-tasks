class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Create a dummy node that points to the head
    # This handles edge cases like removing the first node
    dummy = ListNode(0)
    dummy.next = head

    fast = slow = dummy

    # Move fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Skip the node to remove
    slow.next = slow.next.next

    return dummy.next  # New head (handles case where head was removed)

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""

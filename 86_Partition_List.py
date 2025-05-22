class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Create two dummy heads for two separate lists
    less_head = ListNode(0)     # For nodes with val < x
    greater_head = ListNode(0)  # For nodes with val >= x

    # Pointers to build the two lists
    less = less_head
    greater = greater_head

    current = head

    # Traverse original list and partition nodes
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    # End the greater list
    greater.next = None

    # Link the two lists together
    less.next = greater_head.next

    # Return the start of the new list (skipping dummy node)
    return less_head.next

"""
Time: O(n) — Traverse the list once
Space: O(1) — No extra data structures, just pointers
"""

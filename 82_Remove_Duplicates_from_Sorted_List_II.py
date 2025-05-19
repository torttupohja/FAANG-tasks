class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # Create a dummy node before the actual head
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy  # prev points to last confirmed non-duplicate
    current = head

    while current:
        # Check for duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            duplicate_val = current.val
            while current and current.val == duplicate_val:
                current = current.next
            prev.next = current  # skip the duplicate sequence entirely
        else:
            # No duplicate — move prev to current
            prev = current
            current = current.next

    return dummy.next  # Return the cleaned-up list

"""
Time complexity O(n)
Space complexity O(1)
"""

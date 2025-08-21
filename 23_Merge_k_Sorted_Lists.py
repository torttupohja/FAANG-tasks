import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    dummy = ListNode()
    curr = dummy

    # Push the head of each list into the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

"""
time complexity: O(N log k), where N is the total number of nodes and k is the number of lists
space complexity: O(k) for the heap
"""

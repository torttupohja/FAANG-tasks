# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummyNode=ListNode(0)
        tail=dummyNode
        curr1=list1
        curr2=list2
        while curr1!=None and curr2!=None:
            if curr1.val<=curr2.val:
                tail.next=curr1
                curr1=curr1.next
            else:
                tail.next=curr2
                curr2=curr2.next
            tail=tail.next
        if curr1==None:
            tail.next=curr2
        else:
            tail.next=curr1
        return dummyNode.next

"""
Time Complexity: O(n + m) — where n and m are lengths of the two input lists.
Space Complexity: O(1) — no extra space is used beyond a few pointers.
"""

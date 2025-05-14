# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r1=r2=''
        t1=l1
        t2=l2
        while t1!=None:
            r1+=str(t1.val)
            t1=t1.next
        while t2!=None:
            r2+=str(t2.val)
            t2=t2.next
        r=int(r1[::-1])+int(r2[::-1])
        r=str(r)[::-1]
        print(r)
        dummy= ListNode(int(r[0]))
        temp=dummy
        for i in range(1,len(r)):
            temp.next=ListNode(int(r[i]))
            temp=temp.next
        return dummy
      
"""
Time complexity:O(N)
Space complexity:O(1)
"""

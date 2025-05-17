class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        if left == right:
            return head

        curr = head
        t = None
        prev = None
        s = None
        v = None
        f = False

        if left == 1:
            f = True
            t = curr

        s1 = 1

        while curr:
            if s1 == left and not f:
                v = prev
                t = curr

            if s1 == right:
                s = curr.next
                curr.next = None
                break

            prev = curr
            curr = curr.next
            s1 += 1

        if not f:
            v.next = None

        ans = self.reverseList(t)
        t.next = s

        if not f:
            v.next = ans

        if f:
            head = ans

        return head

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr = head
        prev = None
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
"""
Time complexity:O(n)
Space complexity:O(1))
"""

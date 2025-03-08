# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        i = 0
        while res is not None:
            res = res.next
            i += 1
        if i == n:
            return head.next
        res = head
        for _ in range(1, i - n):
            res = res.next
        res.next = res.next.next
        return head
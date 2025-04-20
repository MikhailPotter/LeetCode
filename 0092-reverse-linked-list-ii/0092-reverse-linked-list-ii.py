# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        for i in range(left-1):
            cur = cur.next
   
        left_tail = cur
        left_node = cur.next

        cur = cur.next
        prev = None
        for i in range(right - left + 1):
            next_ = cur.next
            cur.next = prev
            prev = cur
            cur = next_
        
        left_tail.next = prev
        left_node.next = cur
        
        return dummy.next
        
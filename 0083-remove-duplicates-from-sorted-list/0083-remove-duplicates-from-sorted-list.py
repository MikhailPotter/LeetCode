# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        res_ = res
        while head:
            curr_ = head.val
            next_ = head.next.val if head.next else None
            if curr_ != next_:
                res_.next = ListNode(curr_)
                res_ = res_.next
            head = head.next if head.next else None
        res = res.next
        return res
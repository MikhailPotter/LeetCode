# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        prev = None
        main_head = head

        while head:
            if head.val == val and prev:
                prev.next = head.next
            elif head.val == val:
                main_head = head.next
            else:
                prev = head
            head = head.next
        return main_head
        
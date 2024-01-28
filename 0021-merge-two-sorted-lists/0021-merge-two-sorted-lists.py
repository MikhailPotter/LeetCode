# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        curr = merged_list
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next if list1.next else None
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next if list2.next else None
            curr = curr.next
            
        while list1:
            curr.next = ListNode(list1.val)
            list1 = list1.next if list1.next else None
            curr = curr.next
            
        while list2:
            curr.next = ListNode(list2.val)
            list2 = list2.next if list2.next else None            
            curr = curr.next
           
        merged_list = merged_list.next
        return merged_list
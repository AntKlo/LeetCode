# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        final = None
        if list1.val < list2.val:
            final = list1
            final.next = self.mergeTwoLists(list1.next, list2)
        else:
            final = list2
            final.next = self.mergeTwoLists(list1, list2.next)
        return final
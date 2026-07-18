# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Space: O(N)
        # Time: O(N)
        dummy = ListNode(val=0, next=None)
        pointer = dummy
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                pointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                pointer.next = ListNode(list2.val)
                list2 = list2.next
            pointer = pointer.next
        if list1 is not None:
            pointer.next = list1
        elif list2 is not None:
            pointer.next = list2

        return dummy.next

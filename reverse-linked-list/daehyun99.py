# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time: O(N)
# Space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pointer = head
        left = None
        while pointer.next is not None:
            right = pointer.next
            pointer.next = left
            left = pointer
            pointer = right
        pointer.next = left
        return pointer

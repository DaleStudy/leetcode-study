# TC: O(N)
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fwd, flw = head, head

        for _ in range(n):
            fwd = fwd.next

        if not fwd:
            return head.next

        while fwd.next:
            fwd = fwd.next
            flw = flw.next

        flw.next = flw.next.next

        return head


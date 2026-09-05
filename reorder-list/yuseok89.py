# TC: O(N)
# SC: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        def rec(right: Optional[ListNode]) -> Optional[ListNode]:
            if not right:
                return head

            left = rec(right.next)

            if not left:
                return None

            if left == right or left.next == right:
                right.next = None
                return None

            nxt_left = left.next
            left.next = right
            right.next = nxt_left

            return nxt_left

        rec(head)


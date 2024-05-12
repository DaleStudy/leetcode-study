# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# TC, SC: O(n), O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None

        head.pos = 0

        while head.next:
            if hasattr(head.next, "pos"):
                return True
            head.next.pos = head.pos + 1
            head = head.next

        return False

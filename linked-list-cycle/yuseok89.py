# TC: O(N)
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False

            slow, fast = slow.next, fast.next.next

        return True


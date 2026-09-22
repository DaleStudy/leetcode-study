# Time: O(N)
# Space: O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        curr = head

        while curr is not None:
            if curr.next in seen:
                return True
            seen.add(curr.next)
            curr = curr.next

        return False

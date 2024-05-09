# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

        # visited = head

        # while visited:
        #     if visited.val == None:
        #         return True

        #     visited.val = None
        #     visited = visited.next

        # return False

        # Both TC:O(n) and SC:O(1), but below one is kinda tricky solution

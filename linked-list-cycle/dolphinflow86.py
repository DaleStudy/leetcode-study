# N is the number of nodes in the linked list.
# TC: O(N) - visits each node at most twice
# SC: O(1) - uses only two pointers without extra space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

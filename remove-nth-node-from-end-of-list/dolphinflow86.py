# N is the number of nodes in the linked list.
# TC: O(N) - single pass using two pointers with an (n + 1) gap
# SC: O(1) - modifies links in place using constant extra variables

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# idea : Two pointer
# Time Complexity : O(length(list))
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next



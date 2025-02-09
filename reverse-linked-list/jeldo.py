# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), n = len(nodes)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail

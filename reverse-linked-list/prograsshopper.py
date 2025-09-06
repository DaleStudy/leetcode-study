# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity: O(n) / memory complexity: O(n)
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        dummy_head = ListNode()
        current = dummy_head
        while stack:
            current.next = ListNode(val=stack.pop(), next=None)
            current = current.next
        return dummy_head.next

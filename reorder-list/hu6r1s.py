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
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        node = dummy = ListNode(-1)
        for i in range(len(stack)):
            if i % 2:
                node.next = stack.pop()
            else:
                node.next = head
                head = head.next
            node = node.next
        node.next = None
        return dummy.next

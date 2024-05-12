# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC, SC: O(n), O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        prev_node = head
        node = prev_node.next
        prev_node.next = None

        while node.next:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        node.next = prev_node

        return node

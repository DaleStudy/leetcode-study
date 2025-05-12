# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Time complexity O(n)
    Space complexity O(1)
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = head.next
        prev = head
        prev.next = None

        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        
        return prev

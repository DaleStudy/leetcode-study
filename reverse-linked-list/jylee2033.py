# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list
        if head is None:
            return head

        prev = None
        cur = head # Start from the head node

        # Traverse until the last node
        while cur.next is not None:
            nxt = cur.next # Store next node
            cur.next = prev # Reverse the link
            prev = cur # Move prev forward
            cur = nxt # Move cur forward

        # Handle the last node
        cur.next = prev
        return cur

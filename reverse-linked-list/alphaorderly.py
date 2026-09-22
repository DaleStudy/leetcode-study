"""
Time Complexity: O(n)
Space Complexity: O(1)

- We use a while loop to traverse the linked list.
- We use a prev pointer to store the previous node.
- We use a head pointer to store the current node.
- We use a old_next pointer to store the next node.
- We use a prev, head = head, old_next to update the prev and head pointers.
- We return the prev pointer.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            prev, head.next, head = head, prev, head.next

        return prev

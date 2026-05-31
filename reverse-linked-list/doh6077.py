# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 206. Reverse Linked List
# 1. Use two pointers 
# 2. one pointer indicates the current node and another pointer indicate the previous node 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr 
            curr = nextNode 
        return prev

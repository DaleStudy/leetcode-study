# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        reversed_node = None
        while node:
            val = node.val
            reversed_node = ListNode(val=val, next=reversed_node)
            node = node.next
        return reversed_node
        
    

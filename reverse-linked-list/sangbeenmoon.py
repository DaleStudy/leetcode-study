# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        p = None
        while cur != None:
            n = ListNode(cur.val, p)
            p = n
            cur = cur.next
        return p
        
        
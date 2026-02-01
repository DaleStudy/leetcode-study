# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
        
        return self.removeNth(head, length-n+1)

    def removeNth(self, head, n):
        if n == 1:
            if not head.next:
                return None
            else:
                return head.next
        else:
            if not head.next:
                return head
            head.next = self.removeNth(head.next, n-1)
            return head
        
    

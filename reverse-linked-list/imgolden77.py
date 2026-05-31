class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr is not None: # once was "while curr.next is not None:" but that showed AttributeError: 'NoneType' object has no attribute 'next'
            if prev:
                post = curr.next
                curr.next = prev
                prev = curr
                curr = post
            else:
                post = curr.next
                prev = curr
                curr.next = None
                curr = post

        return prev
    
# First time, return Curr, but the result was [] so I changed to "return prev" as the new head of the reversed Linked list.


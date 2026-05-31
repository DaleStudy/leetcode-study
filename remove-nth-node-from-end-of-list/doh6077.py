class Solution:
    # 19. Remove Nth Node From End of List
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        #  Calculate Length 
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            
        stop_index = length - n
        
        current = dummy 
        for _ in range(stop_index):
            current = current.next
        
        # Delete the node
        current.next = current.next.next
        
        # Return the start of the list (dummy.next handles if head changed)
        return dummy.next

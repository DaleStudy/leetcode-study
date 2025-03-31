# Time Complexity: O(N) - traverse the list three times: 
#                       (1) find the middle (O(N)), 
#                       (2) reverse the second half (O(N)), 
#                       (3) merge the two halves (O(N)).
# Space Complexity: O(1) - use a few extra pointers, no additional data structures.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list using slow & fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        second = slow.next
        # cut the list into two halves
        slow.next = None  
        prev = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the two halves (alternating nodes)
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

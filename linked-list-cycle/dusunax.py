'''
# 141. Linked List Cycle

use two pointers, Floyd's Tortoise and Hare algorithm

> Tortoise and Hare algorithm  
>- slow pointer moves one step at a time
>- fast pointer moves two steps at a time
>- if there is a cycle, slow and fast will meet at some point
>- if there is no cycle, fast will reach the end of the list

## Time Complexity: O(n)
In the worst case, we need to traverse the entire list to determine if there is a cycle.

## Space Complexity: O(1)
no extra space is used, only the two pointers.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
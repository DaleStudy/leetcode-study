"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution 1: 
Two Pass Algorithm 1 
    - First pass: Count the number of nodes and store the values in the list
    - Second pass: Build the new list without the Nth node from the end

Time complexity: O(N)
    - Two passes are required
Space complexity: O(N)
    - The list stores the values of the nodes
    - The new nodes are created to build the new list
"""

class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        dummy_node = ListNode()
        tail = dummy_node
        _n = len(vals) - n
        vals = vals[:_n] + vals[_n+1:]

        for v in vals:
            tail.next = ListNode(val=v)
            tail = tail.next
        
        return dummy_node.next
    


"""
Solution 2:
Reference: 
    [1] https://leetcode.com/problems/remove-nth-node-from-end-of-list/editorial/
    [2] https://www.algodale.com/problems/remove-nth-node-from-end-of-list/
One Pass Algorithm
    - Use two pointers to maintain a gap of n nodes between them
    - When the first pointer reaches the end, the second pointer will be at the Nth node from the end

Time complexity: O(N)
    - Only one pass is required
Space complexity: O(1)
    - No extra space is required
"""

class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next 

        second.next = second.next.next

        return dummy.next

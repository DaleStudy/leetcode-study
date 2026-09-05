"""
https://leetcode.com/problems/reorder-list/

N: number of nodes
Time: O(N)
Space: O(N)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        nodes[left].next = None

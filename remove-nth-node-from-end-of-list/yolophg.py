# Time Complexity: O(N) - go through the list twice (once to count, once to remove).
# Space Complexity: O(1) - only use a few extra variables.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the total number of nodes in the list
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        # find the position of the node to remove (from the start)
        node_to_remove = N - n

        # if need to remove the first node, just return the second node as the new head
        if node_to_remove == 0:
            return head.next
        
        # traverse again to find the node right before the one we need to remove
        curr = head
        for i in range(N - 1):
            if (i + 1) == node_to_remove:
                # remove the nth node by skipping it
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head

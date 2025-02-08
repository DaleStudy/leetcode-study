# Time Complexity: O(n) - traverse the linked list at most once.
# Space Complexity: O(1) - only use two pointers, no extra memory.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers for fast moves twice as fast as slow.
        fast = head
        slow = head

        # loop the list while fast and fast.next exist.
        while fast and fast.next:
            # move fast pointer two steps.
            fast = fast.next.next
            # move slow pointer one step.
            slow = slow.next

            # if they meet, there's a cycle.
            if fast == slow:
                return True
        # if they don't meet, there's no cycle.
        return False

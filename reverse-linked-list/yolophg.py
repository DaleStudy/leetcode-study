# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # to traverse the original list, starting from head
        current = head
        while current:
            # reverse the link and move to the next node
            prev, prev.next, current = current, prev, current.next

        # prev is now the head of the reversed list
        return prev

# TC : O(n)
# SC : O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases such as removing the first node
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move the right pointer n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        left.next = left.next.next

        # Return the head of the modified list
        return dummy.next

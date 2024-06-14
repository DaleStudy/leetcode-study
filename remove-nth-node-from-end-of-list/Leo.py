class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left = right = head

        for i in range(n):
            right = right.next

        if not right: return head.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next  ## deleting node

        return head

        # TC: O(n), SC: O(1)

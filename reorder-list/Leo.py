class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, curr = None, slow

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        ## TC: O(n), SC: O(1)

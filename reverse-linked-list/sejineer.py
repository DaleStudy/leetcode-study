"""
시간 복잡도: O(N)
공간 복잡도: O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev

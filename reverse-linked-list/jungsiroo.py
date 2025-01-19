class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative way

        """
        prev, curr = None, head
        while curr:
            tmp_nxt = curr.next
            
            curr.next = prev
            prev, curr = curr, tmp_nxt

        return prev
        """

        # Recursive Way
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head # reversing pointer
        head.next = None
        return new_head

        # 둘 다 시간복잡도 O(n)
        # 하지만 재귀의 경우 콜스택에 따른 공간복잡도 O(n)을 소요
        # iterative 방식은 O(1)
                
            

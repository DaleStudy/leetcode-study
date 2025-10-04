class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return
        # 중간 노드 찾기 
        slow, fast = head, head 
        while fast and fast.next: 
            slow = slow.next # 1칸 
            fast = fast.next.next # 2칸 

        # 뒤 구간들을 뒤집는다 
        prev, cur = None, slow.next 
        # 중간노드 기준으로 앞 구간만 떼어놓는다 
        slow.next = None

        while cur: 
            nxt = cur.next # 다음 노드 기억 
            cur.next = prev
            prev = cur 
            cur = nxt
        # 앞, 뒤 구간들을 병합 
        first, second = head, prev 
        while second: 
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first, second = n1, n2

            

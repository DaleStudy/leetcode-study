class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        def remove_node(node):
            if node is None:
                return 0
            # 2. 재귀 호출
            count = remove_node(node.next) + 1
            # 4. 삭제 로직 (count가 n+1일 때)
            if count == n + 1:
                node.next = node.next.next
            # 5. 현재 count 반환
            return count

        # 재귀 함수 호출 시작
        total_count = remove_node(head)
        
        if total_count == n:
            return head.next
        return head


# Two Pointer Solution
# One loop 

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        # 삭제할 노드의 바로 전 노드에 도착
        for _ in range(n+1):
            first = first.next
        
        dummy = ListNode(None, head)
        second = dummy 

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

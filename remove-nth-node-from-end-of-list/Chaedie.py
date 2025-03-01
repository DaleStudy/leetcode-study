"""
Solution:
    재귀를 통해 끝까지 간뒤 n번째 pop 될때 노드를 삭제해준다.
Time: O(n)
Space: O(n)
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        count = 0

        def dfs(node, prev):
            nonlocal count
            if not node:
                return

            dfs(node.next, node)
            count += 1
            if count == n:
                prev.next = node.next

        dfs(head, dummy)
        return dummy.next


"""
Solution: 
    1) 2 Pointer 로 size - n 까지 이동
    2) prev 와 curr.next 를 연결
Time: O(n)
Space: O(1)
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = tail = head

        while n > 0:
            tail = tail.next
            n -= 1

        while tail:
            prev = prev.next
            curr = curr.next
            tail = tail.next
        
        prev.next = curr.next
        
        return dummy.next

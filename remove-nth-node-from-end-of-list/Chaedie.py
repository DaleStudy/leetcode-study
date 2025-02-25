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

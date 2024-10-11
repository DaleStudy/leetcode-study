class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited = set()
        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False

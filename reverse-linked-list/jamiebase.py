"""
# Approach
이전 노드, 현재 노드, 다음 노드를 저장한 뒤, 현재 노드가 이전 노드를 가리키도록 방향을 바꾸고,
이전 노드와 현재 노드 포인터를 이동시킵니다.

# Complexity
List의 길이를 N이라고 할 떄
- Time complexity: O(N)
- Space complexity: O(1)
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next  # 1. 다음 노드 저장
            cur.next = prev  # 2. 방향 뒤집기
            prev = cur  # 3. prev 이동
            cur = nxt  # 4. cur 이동
        return prev

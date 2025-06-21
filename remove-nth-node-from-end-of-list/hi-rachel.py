"""
뒤에서 n번째 노드를 없애고, linked list head를 반환해라
TC: O(N), 리스트 한 번 순회
SC: O(1), 포인터 2개만 사용
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node를 head 앞에 두어 edge case(head 삭제 등) 처리
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # first를 n+1칸 먼저 이동 -> 두 포인터 사이 간격이 n
        for _ in range(n + 1):
            first = first.next

        # first가 끝에 도달할 때까지 두 포인터 함께 전진
        while first:
            first = first.next
            second = second.next

        # second의 다음 노드가 삭제 대상이므로 연결 건너뛰기
        second.next = second.next.next

        # 실제 head는 dummy.next에 있음
        return dummy.next

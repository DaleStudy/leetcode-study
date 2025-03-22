'''
시간 복잡도: O(n)
공간 복잡도: O(1)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 리스트 총 길이 계산
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 리스트 길이 계산
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next

        # 제거할 노드가 첫 번째(head)인 경우
        if n == length:
            return head.next

        index = 0
        current = head

        # 제거 대상 노드 전까지 이동
        for _ in range(length - n - 1):
            current = current.next
        
        # 제거 대상 노드 건너뛰기
        current.next = current.next.next

        return head

# Two-Pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head

        # 1. `first`를 n 만큼 이동 → `second`와의 간격 유지
        for _ in range(n):
            first = first.next
        
        # 제거 대상이 첫번째 노드인 경우, next 반환
        if not first:
            return head.next

        # 2. `first`가 끝까지 갈 때까지 `second`도 함께 이동
        while first.next:
            first = first.next
            second = second.next

        # 3. `second.next`가 가리키는 노드 제거
        second.next = second.next.next

        return head

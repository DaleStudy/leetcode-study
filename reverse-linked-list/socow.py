"""
📚 206. Reverse Linked List

📌 문제 요약
- 단방향 연결 리스트가 주어졌을 때, 리스트를 뒤집어서 반환하기
- 예: 1→2→3→4→5 → 5→4→3→2→1

🎯 핵심 알고리즘
- 패턴: 반복 (Iterative) / 재귀 (Recursive)
- 시간복잡도: O(n)
- 공간복잡도: O(1) (반복) / O(n) (재귀 - 콜스택)

💡 핵심 아이디어
1. prev = None, curr = head로 시작
2. 각 노드에서 next를 저장 → curr.next를 prev로 변경
3. prev = curr, curr = next로 이동
4. curr이 None이 되면 prev가 새로운 head!
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 반복 방식 (Iterative)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 다음 노드 저장
            curr.next = prev       # 방향 뒤집기
            prev = curr            # prev 이동
            curr = next_node       # curr 이동
        
        return prev


# 재귀 방식 (Recursive)
class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 빈 리스트 또는 마지막 노드
        if not head or not head.next:
            return head
        
        # 재귀: 나머지 리스트 뒤집기
        new_head = self.reverseList(head.next)
        
        # 현재 노드의 다음 노드가 나를 가리키게 함
        head.next.next = head
        head.next = None
        
        return new_head


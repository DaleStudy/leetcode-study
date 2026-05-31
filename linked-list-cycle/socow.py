"""
📚 141. Linked List Cycle

📌 문제 요약
- 연결 리스트에 사이클(순환)이 있는지 확인하기
- 있으면 True, 없으면 False

🎯 핵심 알고리즘
- 패턴: 플로이드 순환 탐지 (토끼와 거북이)
- 시간복잡도: O(n)
- 공간복잡도: O(1)

💡 핵심 아이디어
1. slow는 한 칸씩, fast는 두 칸씩 이동
2. 사이클이 있으면 → 둘이 언젠가 만남!
3. 사이클이 없으면 → fast가 끝에 도달 (None)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        # 거북이: 한 칸
            fast = fast.next.next   # 토끼: 두 칸
            
            if slow == fast:        # 만났다!
                return True
        
        return False  # fast가 끝에 도달 = 사이클 없음


"""
100. Same Tree

문제 요약
- 두 이진 트리가 똑같은지 확인하기
- 구조도 같고, 값도 같아야 True

문제 예시
트리1:     트리2:
   1          1
  / \        / \
 2   3      2   3
→ True (완전 동일!)

트리1:     트리2:
   1          1
  /            \
 2              2
→ False (구조가 다름!)

핵심 알고리즘
- 패턴: 재귀 (DFS)
- 시간복잡도: O(n) - 모든 노드 방문
- 공간복잡도: O(h) - h는 트리 높이

핵심 아이디어
1. 둘 다 None → True
2. 하나만 None → False
3. 값이 다름 → False
4. 왼쪽 서브트리 비교 & 오른쪽 서브트리 비교
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘 다 None → 같음!
        if not p and not q:
            return True
        
        # 하나만 None → 다름!
        if not p or not q:
            return False
        
        # 값이 다름 → 다름!
        if p.val != q.val:
            return False
        
        # 왼쪽끼리 비교 AND 오른쪽끼리 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

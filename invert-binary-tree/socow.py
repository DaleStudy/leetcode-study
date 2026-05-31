"""
📚 226. Invert Binary Tree

📌 문제 요약
- 이진 트리를 좌우로 뒤집기 (거울처럼!)
- 모든 노드에서 왼쪽 자식 ↔ 오른쪽 자식 교환

📝 문제 예시
    입력:         출력:
       4            4
      / \          / \
     2   7   →    7   2
    / \ / \      / \ / \
   1  3 6  9    9  6 3  1

🎯 핵심 알고리즘
- 패턴: 재귀 (DFS) / 반복 (BFS)
- 시간복잡도: O(n) - 모든 노드 방문
- 공간복잡도: O(h) - h는 트리 높이 (콜스택)

💡 핵심 아이디어
1. 현재 노드의 왼쪽/오른쪽 자식을 swap
2. 왼쪽 서브트리 재귀적으로 뒤집기
3. 오른쪽 서브트리 재귀적으로 뒤집기
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 재귀 방식 (가장 간단!)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 왼쪽 ↔ 오른쪽 swap!
        root.left, root.right = root.right, root.left
        
        # 자식들도 재귀적으로 뒤집기
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


# BFS 방식 (반복)
class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # swap!
            node.left, node.right = node.right, node.left
            
            # 자식들 큐에 추가
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

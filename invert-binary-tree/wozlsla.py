from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
- L/R 노드의 위치 변경 반복 - 재귀/반복
- 트리 순회: 반복문->BFS(Queue)
    1. 큐에 현재 노드 추가
    2. 큐에서 노드 꺼냄
    3. 꺼낸 노드의 왼쪽<->오른쪽 자식 위치 변경
    4. 위치를 바꾼 자식 노드들이 있다면, 다시 큐에 삽입
    5. 큐가 빌 때까지 반복
"""

from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        que = deque([root])

        while que:
            node = que.popleft()

            # 노드의 왼쪽과 오른쪽 자식 교환
            node.left, node.right = node.right, node.left

            # 바꾼 자식 노드들이 있으면 큐에 추가 (하나만 있거나 없는 경우 처리)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return root

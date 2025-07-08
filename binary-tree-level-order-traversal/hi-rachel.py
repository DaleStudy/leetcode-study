"""
주어진 이진 트리를 위에서 아래로, 왼쪽에서 오른쪽으로 레벨 단위로 순회하여
각 레벨에 있는 노드들의 값을 리턴하는 문제

TC: O(N), 모든 노드를 한 번씩 방문
SC: O(N), 큐와 결과 리스트에 최대 N개의 노드 저장 가능
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        queue = deque([root])
        
        while queue:
            # 현재 레벨에 있는 모든 노드들의 값을 리스트에 담기
            level = [node.val for node in queue]
            output.append(level)

            # 현재 레벨에 있는 모든 노드 탐색
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output

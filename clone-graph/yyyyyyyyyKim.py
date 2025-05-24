"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # 깊은 복사
        # DFS 이용했으나 나중에 BFS로도 해 볼 것
        # 시간복잡도 O(n), 공간복잡도 O(n)

        if not node:
            return None

        # 원본에서 복사노드 매핑 저장할 딕셔너리
        copied = {}

        def dfs(curr):
            # 현재 노드가 복사된 노드면 그대로 리턴
            if curr in copied:
                return copied[curr]

            copy = Node(curr.val)   # 현재 노드 복사
            copied[curr] = copy     # 복사본 저장

            # 이웃노드들 복사해서 연결
            for i in curr.neighbors:
                copy.neighbors.append(dfs(i))

            return copy
        
        return dfs(node)

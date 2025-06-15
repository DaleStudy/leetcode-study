"""
- 정점 개수 n, 간선 배열 edges
- 무방향 그래프

트리 조건
1. 완전히 연결된 그래프여야 함 -> 전체 탐색 가능
2. 그래프에 순환하는 부분이 없어야 함

트리 특성상 항상 e = n - 1, 즉 간선의 수 = 노드의 개수 - 1

TC: O(n)
SC: O(n)
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def has_cycle(node, prev):
            # 이미 방문 = 순환 -> 트리 x
            if node in visited:
                return True
            visited.add(node)
            for adj in graph[node]:
                if adj == prev:
                    continue
                if has_cycle(adj, node):
                    return True

            return False
        
        if has_cycle(0, -1):
            return False

        return len(visited) == n

'''
Time Complexity: O(N + E)
- 노드의 개수 N, 간선의 개수 E
- 노드의 개수와 간선의 수를 합친만큼 재귀 함수 호출 필요 

Space Complexity: O(N + E)
- 인접 리스트의 크기가 노드와 간선의 수의 합에 비례 
- 집합에 최대 N개의 숫자 저장
'''
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # 연결관계를 표현하기 위한 그래프
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 깊은탐색에서 노드 방문여부 표기 
        visited = set()

        def dfs(node):
        # 재귀함수 실행시 방문 처리
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)
        
        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count

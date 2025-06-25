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

        # DFS
        # 시간 복잡도 O(n + e), 공간복잡도 O(n + e) // n=노드수, e=간선수
        # 인접 리스트 방식으로 무방향 그래프 생성
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set() # 방문한 노드 저장할 집합
        answer = 0      # 연결 요소 개수

        # 현재 node와 연결된 모든 노드 방문 처리하는 함수
        def dfs(node):
            # 이미 방문한 노드라면 dfs 종료
            if node in visited:
                return
            visited.add(node)   # node 방문처리
            # 연결된 노드들도 탐색
            for i in graph[node]:
                dfs(i)

        # 모든 노드 탐색 후 연결 요소 개수 세기
        for i in range(n):
            # 방문하지 않은 노드라면 dfs 탐색하고 연결요소(answer) +1
            if i not in visited:
                dfs(i)
                answer += 1

        return answer

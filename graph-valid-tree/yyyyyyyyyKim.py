from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # DFS(그래프 탐색)
        # 시간복잡도 O(n), 공간복잡도 O(n)

        # 트리의 간선 수는 항상 "노드 수 -1"(아니면 바로 False)
        if len(edges) != n-1:
            return False

        # 인접 리스트 방식으로 그래프 생성
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # set사용(방문여부만 빠르게 탐색(in연산 시간복잡도 O(1))
        visited = set()

        def dfs(node,prev):
            # 이미 방문한 노드면 종료
            if node in visited:
                return
            visited.add(node)

            # 현재 노드와 이웃 탐색
            for i in graph[node]:
                # 바로 이전 노드 패스(무방향 그래프니까)
                if i == prev:
                    continue
                dfs(i, node)


        # 0번 노드부터 탐색 시작
        dfs(0, -1)

        # 방문한 노드 수와 전체 노드 수가 같으면 연결 그래프 -> 트리
        return len(visited) == n

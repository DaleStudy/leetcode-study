from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        - Idea: 유효한 트리라면 만족해야 하는 조건들을 활용하여 트리 여부를 판단한다.
        - Time Complexity: O(v + e). v와 e는 각각 노드의 수, 연결된 선(엣지)의 수
            인접 리스트로 만든 그래프를 순회할 때, 노드마다 연결된 엣지를 따라가며 탐색하므로 O(v + e)이 소요된다.
        - Space Complexity: O(v + e). v와 e는 각각 노드의 수, 엣지의 수
            그래프를 인접 리스트로 저장하기 위해 O(v + e)의 공간이 필요하다.

        """
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()

        def DFS(v: int) -> None:
            visited.add(v)

            for adj in graph[v]:
                if adj not in visited:
                    DFS(adj)

        DFS(0)

        return len(visited) == n

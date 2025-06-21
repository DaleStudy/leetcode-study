# https://leetcode.com/problems/graph-valid-tree/

from typing import List

class Solution:
    def validTree_bfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        [Complexity] (첫 번째 조건을 통과하면 e = n - 1일 것이므로, n으로 변환도 가능)
            - TC: O(v + e) (== O(n + len(edges)))
            - SC: O(v + e) (graph)

        [Approach]
            valid tree란 다음의 두 조건을 만족하는 undirected graph이다.
                1) acyclic      -> edges의 개수가 n - 1개인지 확인 (-> early stop 가능)
                2) connected    -> 모든 node가 모두 방문되었는지, 즉 len(visited) == n인지 확인

            이러한 조건을 BFS로 확인할 수 있다.
        """
        from collections import deque

        # edge의 개수가 n - 1이 아니라면 빠르게 반환 (-> acyclic & connected 여부 확인)
        if len(edges) != n - 1:
            return False

        # undirected graph 구성
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 0번 노드부터 시작
        visited = {0}
        q = deque([0])

        # BFS
        while q:
            pos = q.popleft()
            for npos in graph[pos]:
                if npos not in visited:
                    visited.add(npos)
                    q.append(npos)

        # visited에 모든 노드가 들어가있다면 true (-> connected 여부 확인)
        return len(visited) == n

    def validTree_dfs(self, n: int, edges: List[List[int]]) -> bool:
        """
        [Complexity]
            - TC: O(v + e) (== O(n + len(edges)))
            - SC: O(v + e) (graph) (call stack의 경우 O(v))

        [Approach]
            valid tree의 조건을 DFS로 확인할 수 있다.
        """
        # edge의 개수가 n - 1이 아니라면 빠르게 반환 (-> acyclic & connected 여부 확인)
        if len(edges) != n - 1:
            return False

        # undirected graph 구성
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(pos):
            # base condition
            if pos in visited:
                return

            # visit 처리
            visited.add(pos)

            # recur
            for npos in graph[pos]:
                dfs(npos)

        dfs(0)

        # visited에 모든 노드가 들어가있다면 true (-> connected 여부 확인)
        return len(visited) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        [Complexity]
            - TC: O(e * α(v))
                - e 만큼 반복
                - 각 union-find는 path compression으로 인해 α(v)이며, 이는 거의 상수
                => e = n - 1이므로 O(n)으로도 표현 가능
            - SC: O(n)

        [Approach]
            union-find로 undirected graph의 cycle 여부를 판단할 수 있다.
            따라서 valid tree의 두 조건 중 connected 조건을 확인할 때 union-find를 사용할 수 있다.
                1) acyclic      -> edges의 개수가 n - 1개인지 확인 (-> early stop 가능)
                2) connected    -> union-find 시 parent가 같은 경우가 있는지 확인
        """
        # edge의 개수가 n - 1이 아니라면 빠르게 반환 (-> acyclic & connected 여부 확인)
        if len(edges) != n - 1:
            return False

        # union-find functions
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_parent(x, y):
            px, py = find_parent(x), find_parent(y)

            # cyclic 하다면(= x와 y의 parent가 같다면) False 반환
            if px == py:
                return False

            # union
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

            return True

        # perform union-find
        parent = [i for i in range(n)]
        for x, y in edges:
            if not union_parent(x, y):
                return False

        return True

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from typing import List

class Solution:
    def countComponents_bfs(self, n: int, edges: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(v + e) (모든 edge & node 한 번씩 탐색)
            - SC: O(v + e) (graph)

        [Approach]
            BFS로 visited를 기록해가며 connected component를 센다.
        """
        from collections import deque

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited, res = set(), 0

        def bfs(start):
            q = deque([start])
            visited.add(start)

            while q:
                pos = q.popleft()
                for npos in graph[pos]:
                    if npos not in visited:
                        q.append(npos)
                        visited.add(npos)

            return

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1

        return res

    def countComponents_dfs(self, n: int, edges: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(v + e) (모든 edge & node 한 번씩 탐색)
            - SC: O(v + e) (graph)

        [Approach]
            DFS로 visited를 기록해가며 connected component를 센다.
        """
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited, res = set(), 0

        def dfs(pos):
            # 이전에 visited 포함 여부 확인하므로 base condition 생략 가능

            visited.add(pos)

            # recur
            for npos in graph[pos]:
                if npos not in visited:
                    dfs(npos)

            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(v + e * α(v)) (모든 edge & node 한 번씩 탐색)
            - SC: O(v) (parent, set(...))

        [Approach]
            edges를 iterate 하며 union-find 수행 후, parent의 종류의 개수를 세면 된다.
            parent의 종류의 개수를 셀 때는 다시 find_parent(x)로 찾아야 한다!
        """

        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union_parent(x, y):
            px, py = find_parent(x), find_parent(y)

            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        parent = [i for i in range(n)]

        for x, y in edges:
            union_parent(x, y)

        return len(set(find_parent(i) for i in range(n)))

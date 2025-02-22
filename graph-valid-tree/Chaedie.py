"""
Conditions of Valid Tree
1) no Loop
2) all nodes has to be connected

Time: O(node + edge)
Space: O(node + edge)
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) != n - 1:
            return False

        # Make Graph
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        # loop check
        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in graph[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, None) and n == len(visit)

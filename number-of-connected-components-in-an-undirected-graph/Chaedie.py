"""
Solution: 
    인접 그래프를 그려준다.
    dfs 해준다.
    중복제거를 위해 visit set 을 사용해야한다.
    모든 노드에 대해 dfs 를 하되 갯수를 count 한다.
Time: O(n)
Space: O(n)
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # 인접 리스트
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for i in graph[node]:
                if i not in visit:
                    dfs(i)

        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count

from collections import deque, defaultdict

class Solution:
    """
        - Time Complexity: O(n + e), e = len(edges)
        - Space Complexity: O(n), The size of dictionary
    """
    def validTree(self, n, edges):
        # The number of edges must be "n - 1"
        if len(edges) != n - 1:
            return False

        dic = defaultdict(list)
        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)

        # BFS for visiting all nodes
        visited = set()
        dq = deque([0])

        while dq:
            node = dq.popleft()
            if node in visited:
                continue
            visited.add(node)
            for next in dic[node]:
                if next not in visited:
                    dq.append(next)

        # Check all nodes were visited
        return len(visited) == n

tc = [
        (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
        (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False)
]

sol = Solution()
for i, (n, edges, e) in enumerate(tc, 1):
    r = sol.validTree(n, edges)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

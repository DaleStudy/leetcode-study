# V is the number of nodes (n), and E is the number of edges.
# TC: O(V + E) - builds adjacency list and traverses graph with DFS
# SC: O(V + E) - stores graph adjacency list and stack/visited set


class Solution:

    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set([0])
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return len(visited) == n

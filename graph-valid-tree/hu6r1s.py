if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for node, adj in edges:
            graph[node].append(adj)
            graph[adj].append(node)

        visited = set()

        def dfs(node):
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)

        dfs(0)
        return len(visited) == n

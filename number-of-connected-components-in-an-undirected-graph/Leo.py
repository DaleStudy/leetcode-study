class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = collections.defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        count = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                count += 1

        return count

        ## TC && SC: O(num(edge) + num(node))

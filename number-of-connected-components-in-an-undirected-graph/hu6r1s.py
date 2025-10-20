class Solution:
    # def countComponents(self, n: int, edges: List[List[int]]) -> int:
    #     graph = [[] for _ in range(n)]
    #     for node, adj in edges:
    #         graph[node].append(adj)
    #         graph[adj].append(node)

    #     visited = set()

    #     def dfs(node):
    #         visited.add(node)
    #         for adj in graph[node]:
    #             if adj not in visited:
    #                 dfs(adj)

    #     cnt = 0
    #     for node in range(n):
    #         if node not in visited:
    #             cnt += 1
    #             dfs(node)
    #     return cnt


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for node, adj in edges:
            graph[node].append(adj)
            graph[adj].append(node)

        cnt = 0
        visited = set()
        for node in range(n):
            if node in visited:
                continue
            cnt += 1
            queue = deque([node])
            while queue:
                node = queue.pop()
                visited.add(node)
                for adj in graph[node]:
                    if adj not in visited:
                        queue.append(adj)
        return cnt

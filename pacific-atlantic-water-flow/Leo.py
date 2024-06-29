class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and heights[new_x][new_y] >= \
                        heights[x][y]:
                    dfs(visited, new_x, new_y)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)

        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)

        return list(p_visited.intersection(a_visited))

        ## TC: O(mn), SC: O(mn)

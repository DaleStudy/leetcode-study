from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x, y):
            queue = deque([(x, y)])
            grid[x][y] = "0"

            while queue:
                r, c = queue.popleft()

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        n, m = len(grid), len(grid[0])

        dr = (-1, 1, 0, 0)
        dc = (0, 0, -1, 1)

        result = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    bfs(r, c)
                    result += 1

        return result

"""
시간 복잡도: O(m * n)
공간 복잡도: O(m * n)
"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not vis[i][j]:
                    queue = deque()
                    queue.append((j, i))
                    vis[i][j] = True
                    while queue:
                        cur = queue.popleft()
                        for nxt in range(4):
                            nx = cur[0] + dx[nxt]
                            ny = cur[1] + dy[nxt]
                            if not 0 <= nx < n or not 0 <= ny < m:
                                continue
                            if vis[ny][nx] or grid[ny][nx] != '1':
                                continue
                            queue.append((nx, ny))
                            vis[ny][nx] = True
                    result += 1
        
        return result

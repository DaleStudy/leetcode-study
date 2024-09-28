# 시간복잡도: O(M*N)
# 공간복잡도: O(M*N)

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        m = len(grid)
        n = len(grid[0])
        q = deque()

        def bfs(a, b):
            q.append((a, b))
            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if not (0 <= nx < m and 0 <= ny < n): continue

                    if grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count

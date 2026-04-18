"""
Time Complexity: O(m * n)
Space Complexity: O(m * n)

과정:
1. 2차원 배열을 순회하면서 1을 만나면 섬의 개수를 증가시킴
2. DFS를 통해 해당 섬을 탐색함
3. 해당 섬을 탐색하면서 0을 만나면 탐색을 종료함
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid[0]), len(grid)
        visited = [[0] * m for _ in range(n)]
        dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
        for y in range(n):
            for x in range(m):
                if int(grid[y][x]) == 1 and visited[y][x] == 0:
                    ans += 1
                    dfs = [(x, y)]
                    visited[y][x] = 1
                    while dfs:
                        cx, cy = dfs.pop(0)
                        for _dx, _dy in zip(dx, dy):
                            gy = cy + _dy
                            gx = cx + _dx
                            if gx >= 0 and gy >= 0 and gx < m and gy < n and int(grid[gy][gx]) == 1 and visited[gy][gx] == 0:
                                visited[gy][gx] = 1
                                dfs.append((gx, gy))
        return ans

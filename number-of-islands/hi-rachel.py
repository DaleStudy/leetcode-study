"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

BFS 풀이
TC: O(m * n)
SC: O(m * n)
"""

from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            grid[x][y] = 2

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == "1":
                            grid[nx][ny] = "2"
                            queue.append((nx, ny))

            return True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    if bfs(i, j):
                        ans += 1

        return ans

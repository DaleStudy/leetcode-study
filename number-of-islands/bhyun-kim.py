"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Solution:
    To solve this problem, we can use a depth-first search (DFS) to explore all connected land cells.
    We can create a helper function that takes the current cell and marks it as visited.
    
    - We can iterate through all cells in the grid.
    - If the current cell is land, we explore all connected land cells using DFS.
    - We mark all connected land cells as visited.
    - We increment the island count by 1.

Time complexity: O(m x n)
    - m and n are the dimensions of the grid.
    - We explore all cells in the grid once.

Space complexity: O(m x n)
    - We use a recursive call stack to explore all connected land cells.
    - The maximum depth of the call stack is the number of cells in the grid.

"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        island_count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '#'

            dfs(i - 1, j)  
            dfs(i + 1, j)  
            dfs(i, j - 1)  
            dfs(i, j + 1)  

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':
                    dfs(i, j)
                    island_count += 1

        return island_count

        
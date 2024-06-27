"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/

Solution:
    To solve this problem, we can use depth-first search (DFS) to explore all possible paths starting from each cell.
    We can create a helper function that takes the current cell and marks it as reachable.

    - We can create two sets to store the cells that are reachable from the Pacific and Atlantic oceans.
    - We can start DFS from the cells on the borders of the Pacific and Atlantic oceans.
    - We can find the intersection of the two sets to get the cells that are reachable from both oceans.


Time complexity: O(m x n)
    - m and n are the dimensions of the grid.
    - We explore all cells in the grid once.

Space complexity: O(m x n)
    - We use two sets to store the reachable cells from the Pacific and Atlantic oceans.
    - The maximum size of the sets is the number of cells in the grid.
"""


from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        def dfs(matrix, reachable, x, y):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            reachable.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and (nx, ny) not in reachable
                    and matrix[nx][ny] >= matrix[x][y]
                ):
                    dfs(matrix, reachable, nx, ny)

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        for i in range(m):
            dfs(heights, pacific_reachable, i, 0)
            dfs(heights, atlantic_reachable, i, n - 1)

        for j in range(n):
            dfs(heights, pacific_reachable, 0, j)
            dfs(heights, atlantic_reachable, m - 1, j)

        return list(pacific_reachable & atlantic_reachable)

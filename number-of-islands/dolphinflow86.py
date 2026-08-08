# R is the number of rows, and C is the number of columns.
# TC: O(R * C) - visits each cell at most once
# SC: O(R * C) - uses the recursion stack in the worst case
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0])

        def dfs(row, col):
            if (
                row < 0
                or row >= row_count
                or col < 0
                or col >= column_count
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        island_count = 0

        for row in range(row_count):
            for col in range(column_count):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)

        return island_count

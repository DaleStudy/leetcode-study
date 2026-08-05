class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def dfs(row: int, col: int):
            if not (0 <= row < row_len and 0 <= col < col_len):
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        num_islands = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands

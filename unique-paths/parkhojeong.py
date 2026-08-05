class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * m
        grid = [row] * n
        grid[0][0] = 1

        row_len = len(grid)
        col_len = len(row)

        def get_unique_path(row, col):
            if row == 0 and col == 0:
                return grid[0][0]

            if row == 0:
                return grid[row][col - 1]

            if col == 0:
                return grid[row - 1][col]

            return grid[row - 1][col] + grid[row][col - 1]


        for row in range(row_len):
            for col in range(col_len):
                grid[row][col] = get_unique_path(row, col)

        return grid[-1][-1]

class Solution:
    # O(m*n), m = len(grid), n = len(grid[0])
    def numgrids(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return
            if grid[i][j] == "-1" or grid[i][j] == "0":
                return
            grid[i][j] = "-1"
            for d in dirs:
                dfs(i + d[0], j + d[1])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count

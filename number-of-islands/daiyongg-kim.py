if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        island_count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            grid[i][j] = "#"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    island_count += 1

        return island_count

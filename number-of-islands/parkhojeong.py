class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        num_islands = 0
        stack = []

        def is_bound(r, c):
            return 0 <= r < row_len and 0 <= c < col_len

        def is_land(r, c):
            return grid[r][c] == "1"

        for row in range(row_len):
            for col in range(col_len):
                if not is_land(row, col):
                    continue

                stack.append((row, col))
                grid[row][col] = "0"
                num_islands += 1

                while stack:
                    r, c = stack.pop()

                    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        next_r, next_c = r + dr, c + dc

                        if is_bound(next_r, next_c) and is_land(next_r, next_c):
                            grid[next_r][next_c] = "0"
                            stack.append((next_r, next_c))

        return num_islands

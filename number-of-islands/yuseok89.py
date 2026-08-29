# TC: O(NM)
# SC: O(NM)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def fill(row: int, col: int):
            grid[row][col] = '0'

            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]

                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == '1':
                    fill(new_row, new_col)

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == '1':
                    fill(i, j)
                    ans += 1

        return ans


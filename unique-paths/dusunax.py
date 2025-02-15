'''
# 62. Unique Paths

use dynamic programming & a dp table to store the number of ways to reach each cell.

### TC is O(m * n):
- iterating through every cell in the grid. = O(m * n)
- updating each cell in the grid. = O(1)

### SC is O(m * n):
- using a dp table (2D array) to store the number of ways to reach each cell. = O(m * n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[m - 1][n - 1]

# dp[r][c] = dp[r-1][c] + dp[r][c-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # $Paths(r, c) = Paths(r-1, c) + Paths(r, c-1)$

        dp = [ [1] * n for _ in range(m) ]

        # DP Approach
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

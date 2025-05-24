"""
Time, space complexity O(m*n)

Dynamic programming
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(n):
                if i == 0:
                    continue
                if j == 0:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]

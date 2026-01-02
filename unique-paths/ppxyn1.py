# idea : - 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([0]*n)
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                val = 0
                if i > 0:
                    val += dp[i-1][j]
                if j > 0:
                    val += dp[i][j-1]
                dp[i][j] = val
        return dp[m-1][n-1]




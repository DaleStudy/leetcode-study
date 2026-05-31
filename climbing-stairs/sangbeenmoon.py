# dp[i] = dp[i-2] + dp[i-1]
# time : O(n)
# complexity : O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        if n == 1:
            return dp[0]
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n-1]        

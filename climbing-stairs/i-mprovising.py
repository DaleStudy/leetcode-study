"""
Time complexity O(n)
Space complexity O(n)

Dynamic programming
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2] # distinct ways to reach i steps
        if n <= 2:
            return dp[n]
        
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

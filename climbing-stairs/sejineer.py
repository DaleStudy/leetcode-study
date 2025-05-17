"""
시간 복잡도: O(N)
공간 복잡도: O(N)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

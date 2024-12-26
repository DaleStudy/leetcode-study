class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dynamic programming
        dp[0] = 1
        dp[1] = 1
        dp[2] = dp[0] + dp[1] = 2
        dp[3] = dp[1] + dp[2] = 3
        ...

        Tc = O(n) / Sc = O(n)
        """

        dp = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
        

class Solution:
    # Space complexity: O(1)
    # Tiem complexity: O(n)
    def climbStairs(self, n: int) -> int:
        # dp[0] is n - 2
        # dp[1] is n - 1
        dp = [1, 2]

        if n <= 2: 
            return dp[n - 1]
        
        for i in range(3, n + 1): 
            # dp[n] = dp[n - 1] + dp[n - 2]
            #       = dp[1] + dp[0]
            dp[(i - 1) % 2] = sum(dp)
        
        return dp[(n - 1) % 2]

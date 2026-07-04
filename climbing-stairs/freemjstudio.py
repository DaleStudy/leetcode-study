class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0 
        if n == 1: # ways(1) = 1
            return 1

        if n == 2: # ways(2) = 2
            return 2
        
        dp = [0] * 46 # 1 <= n <= 45
        dp[1] = 1
        dp[2] = 2

        # 점화식 : ways(n) = ways(n-1) + ways(n-2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
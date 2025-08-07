class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]

        for i in range(1,n+1):
            if i == 1 or i == 2:
                dp.append(i)
                continue

            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]

class Solution:
    def climbStairs(self, n: int) -> int:
            if n <= 1:
                return 1

            # dp = [0] * (n + 1)
            # dp[0] = 1
            # dp[1] = 1

            # for i in range(2, n + 1):
            #     dp[i] = dp[i - 1] + dp[i - 2]

            # return dp[n]
            # optima sol
            dp_0,dp_1=1,1
            for _ in range(2,n+1):
                dp_0,dp_1=dp_1,dp_0+dp_1
            return dp_1




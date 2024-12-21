'''
solution: 
    # dp[1] = 1step = 1
    # dp[2] = (1step + 1step) + 2step = 2
    # dp[3] = (dp[3 - 1] + 1step) + dp[3 - 2] + 2step = 2 + 1 = 3
    # dp[4] = (dp[4 - 1] + 1step) + (dp[4 - 2] + 2tep) = 3 + 2 = 5

    # dp[n] = (dp[n-1] + 1) + (dp[n-2] + 1)

time O(n)
space O(n)

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]
        dp.append(1)
        dp.append(2)
        
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

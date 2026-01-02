# idea: DP
# I'm not always sure how to approach DP problems. I just try working through a few examples step by step and then check that it would be DP.
# If you have any suggestions for how I can come up with DP, I would appreciate your comments :)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[2], dp[3] = 2, 3
        
        #for i in range(4, n): error when n=4       
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    



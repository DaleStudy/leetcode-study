# idea: DP
# Time Complexity : O(n)
'''
n = 4
-------------------------------
(dp[3] + 1step)
1step + 1step + 1step + 1step 
1step + 2step + 1step
2step + 1step + 1step

(dp[2] + 2step)
1step + 1step + 2step
2step + 2step

================================
n = 5
--------------------------------
(dp[4] + 1step)
1step + 1step + 1step + 1step + 1step
1step + 2step + 1step + 1step
1step + 1step + 2step + 1step
2step + 1step + 1step + 1step
2step + 2step + 1step

(dp[3] + 2step)
1step + 2step + 2step
2step + 1step + 2step
1step + 1step + 1step + 2step
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[2], dp[3] = 2, 3
        
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    



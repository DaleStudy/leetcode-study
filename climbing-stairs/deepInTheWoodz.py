class Solution:
  def climbStairs(self, n: int) -> int:
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+2):
      dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
  
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
        dp = [0] * (n + 1) # n 번째의 계단을 오르는 방법을 찾기 위해 dp배열 생성
        dp[0] = 1
        dp[1] = 1
        # n번째의 계단을 오르기 위해서는 
        # n-1, n-2번째의 계단에서 올수있는 경우의 수들의 합이 n번째 계단을 오르기 위한 모든 경우의 수
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

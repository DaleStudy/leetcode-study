class Solution:
    def climbStairs(self, n: int) -> int:
        """
        To find the number of distinct ways clibe to the top

        time complexity: O(n)
        space complexity: O(n)
        """
        dp = [0] * (n+1)

        for i in range(n+1):
            if i == 0 or i == 1 or i == 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

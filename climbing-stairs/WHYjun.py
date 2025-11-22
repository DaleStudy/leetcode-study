class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.climbStairsRecursively(n, dp)

    def climbStairsRecursively(self, n: int, dp: Dict[int, int]):
        if n == 1:
            dp[1] = 1
            return dp[1]
        if n == 2:
            dp[2] = 2
            return dp[2]

        if n - 2 not in dp:
            dp[n - 2] = self.climbStairsRecursively(n - 2, dp)

        if n - 1 not in dp:
            dp[n - 1] = self.climbStairsRecursively(n - 1, dp)

        return dp[n - 2] + dp[n - 1]

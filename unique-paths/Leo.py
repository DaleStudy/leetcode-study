class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]
        ## TC: O(mn), SC: O(n)

        ## return math.comb(m + n - 2, m - 1)
        ## TC: O(1) whatever constant, SC: O(1)

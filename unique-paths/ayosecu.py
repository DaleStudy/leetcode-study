class Solution:
    """
        - Time Complexity: O(mn)
        - Space Complexity: O(mn), the "dp" variable
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [1] * n for _ in range(m) ]

        # DP Approach
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]

tc = [
        (3, 7, 28),
        (3, 2, 3)
]

sol = Solution()
for i, (m, n, e) in enumerate(tc, 1):
    r = sol.uniquePaths(m, n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

class Solution:
    """
        - Time Complexity: O(n)
        - Space Complexity: O(n)
    """
    def climbStairs(self, n: int) -> int:
        """
            - DP Formation
                - dp[0] = 1
                - dp[1] = 1
                - dp[2] = dp[1] + dp[0] = 2
                - dp[3] = dp[2] + dp[1] = 3
                - dp[i] = dp[i - 1] + dp[i - 2]
        """
        if n <= 1:
            return 1
        
        dp = [1] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]


tc = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5)
]

for i, (n, e) in enumerate(tc, 1):
    sol = Solution()
    r = sol.climbStairs(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

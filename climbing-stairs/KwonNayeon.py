"""
Constraints:
    - 1 <= n <= 45

Time Complexity:
    - O(n)
Space Complexity:
    - O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

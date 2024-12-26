class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] represents the number of distinct ways to climb to the ith step.
        # Base cases:
        # - There is 1 way to reach step 0 (doing nothing).
        # - There is 1 way to reach step 1 (a single step).
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
# Complexity
# - time: O(n)
# - space: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
    
# Complexity
# - time: O(n)
# - space: O(1)

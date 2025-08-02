"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:

- Space complexity:

"""


# DP
class Solution:
    def rob(self, nums: List[int]) -> int:

        # initialize dp array
        dp = [0] * (len(nums) + 1)

        if nums:
            dp[1] = nums[0]

        for n in range(2, len(dp)):
            # current house : nums[n-1]
            rob_current = nums[n - 1] + dp[n - 2]
            skip_current = dp[n - 1]

            dp[n] = max(rob_current, skip_current)

        return dp[-1]


""" Recursive + Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start >= len(nums):
                memo[start] = 0
            else:
                memo[start] = max(nums[start] + dfs(start + 2), dfs(start + 1))

            return memo[start]

        return dfs(0)
"""

""" Recursive
class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(start):
            if start >= nums(len):
                return 0

            return max(nums[start] + dfs[start+2], dfs[start+1])

        return dfs(0)
"""

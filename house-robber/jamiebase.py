"""
# Intuition
DP를 사용한다.

# Approach
특정 집의 최대 money 값 = max(전전집을 털었을 경우의 최댓값 + 현재 집의 money 값, 이전 집을 턴 경우의 최댓값)

# Complexity
- Time complexity: O(N)
- Space complexity: O(N)
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n  # O(N)

        if n == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for house in range(2, n):  # O(N)
            dp[house] = max(dp[house - 1], dp[house - 2] + nums[house])

        return dp[n - 1]

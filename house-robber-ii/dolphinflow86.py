# N is the number of houses.
# TC: O(N) - two passes of linear house robber (excluding first or last house)
# SC: O(1) - constant auxiliary space tracking two variables for DP

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

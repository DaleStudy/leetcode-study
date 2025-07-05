"""
이웃집은 못텀, 주어진 nums list 집은 원형으로 이어져 있음 (맨 처음 <- > 맨 마지막 이웃)
가장 많은 돈을 가지고 있는 집을 최대한으로 턴 총 금액을 반환

1. 첫 집을 포함하고, 마지막 집을 제외하는 경우 nums[:-1]
2. 첫 집을 제외하고, 마지막 집을 포함하는 경우 nums[1:]

TC: O(N),
SC: O(N)
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        def rob_linear(houses: List[int]) -> int:
            if len(houses) == 1:
                return houses[0]
        
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])
            return dp[-1]

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])

        return max(case1, case2)

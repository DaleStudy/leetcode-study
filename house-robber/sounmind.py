from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_length = len(nums)

        if house_length == 0:
            return 0
        if house_length == 1:
            return nums[0]
        if house_length == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])]

        for index in range(2, house_length):
            dp.append(max(dp[index - 1], dp[index - 2] + nums[index]))

        return dp[-1]

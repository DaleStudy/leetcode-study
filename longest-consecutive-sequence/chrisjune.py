from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums = list(set(nums))
        nums.sort()
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        print(dp)
        return max(dp)

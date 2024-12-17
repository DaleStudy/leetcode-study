from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            dpMax = 0
            for j in range(i + 2, len(nums)):
                dpMax = max(dpMax, dp[j])
            dp[i] = nums[i] + dpMax
        
        return max(dp)


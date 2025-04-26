from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [Complexity]
        Time: O(n)
        Space: O(n)
        '''
        cnt = len(nums)

        if cnt == 1:
            return nums[0]
        if cnt == 2:
            return max(nums[0], nums[1])

        dp = [0] * cnt
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, cnt):
            # skip: dp[i-1]
            # rob: dp[i-2]+nums[i]
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return max(dp)

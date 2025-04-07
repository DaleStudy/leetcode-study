"""
Time complexity O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [nums[0], max([nums[0], nums[1]])]
        if n == 2:
            return dp[1]
        
        for i in range(2, n):
            num = nums[i]
            tmp = [
                dp[i-2] + num,
                dp[i-1]
            ]
            dp.append(max(tmp))
        return dp[-1]

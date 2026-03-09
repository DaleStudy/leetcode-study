class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        if len(nums) >= 2:
            dp[1] = max(nums[0], nums[1])
        else:
            return nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        res = list(dp.values())[-1]
        return res

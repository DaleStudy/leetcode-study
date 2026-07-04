class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        max_value = nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(max(max_value, dp[i - 2]) + nums[i], dp[i - 1])

        return dp[-1]

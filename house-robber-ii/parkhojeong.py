class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            max(self.rob_linear(nums[:-1])),
            max(self.rob_linear(nums[1:] ))
        )

    def rob_linear(self, nums: list[int]):
        N = len(nums)

        dp = [0] * (N + 1)
        dp[1] = nums[0]

        for i in range(2, N + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])


        return dp

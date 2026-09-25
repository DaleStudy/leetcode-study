class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        prefix_sum = [0] * (N + 1)
        prefix_sum[1] = nums[0]
        for i in range(2, N):
            prefix_sum[i] = max(prefix_sum[i - 2] + nums[i - 1], prefix_sum[i - 1])

        prefix_sum2 = [0] * (N + 1)
        prefix_sum2[2] = nums[1]
        for i in range(3, N + 1):
            prefix_sum2[i] = max(prefix_sum2[i - 2] + nums[i - 1], prefix_sum2[i - 1])

        return max(max(prefix_sum), max(prefix_sum2))

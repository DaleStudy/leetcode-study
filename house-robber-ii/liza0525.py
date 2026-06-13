class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0 or i == 1:
                dp1[i] = nums[i]
            else:
                dp1[i] = nums[i] + max(dp1[:i - 1])

        nums = nums[1:] + [nums[0]]

        for i in range(len(nums)):
            if i == 0 or i == 1:
                dp2[i] = nums[i]
            else:
                dp2[i] = nums[i] + max(dp2[:i - 1])

        return max(dp1[:-1] + dp2[:-1])

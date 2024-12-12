class Solution:
    # O(n)
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-3], nums[i-2])
        return max(nums[-1], nums[-2])

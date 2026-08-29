class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)

        result = max(nums)
        val = 0
        for i in range(len(nums)-1, -1, -1):
            val += nums[i]
            if val < 0:
                val = 0
            result = max(result, val)

        val = 0
        for i in range(len(nums)):
            val += nums[i]
            if val < 0:
                val = 0
            result = max(result, val)
        return result

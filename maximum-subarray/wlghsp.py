"""
TC : O(N) 
SC: O(1)
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        current = nums[0]
        result = nums[0]

        for i in range(1, n):
            current = max(current + nums[i], nums[i])
            result = max(result, current)
        return result

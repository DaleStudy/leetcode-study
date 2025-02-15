'''
TC : O(n)
SC : O(1)
'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            max_prod, min_prod = max(nums[i], nums[i] * max_prod, nums[i] * min_prod), min(nums[i], nums[i] * min_prod, nums[i] * max_prod)
            result = max(result, max_prod)
        return result

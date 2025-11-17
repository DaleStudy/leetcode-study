class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        min_prod = max_prod = 1
        for num in nums:
            min_prod, max_prod = min(min_prod * num, max_prod * num, num), max(min_prod * num, max_prod * num, num)
            result = max(max_prod, result)
        return result

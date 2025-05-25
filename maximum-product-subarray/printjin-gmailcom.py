class Solution:
    def maxProduct(self, nums):
        max_prod = min_prod = result = nums[0]
        for n in nums[1:]:
            temp_max = max(n, max_prod * n, min_prod * n)
            min_prod = min(n, max_prod * n, min_prod * n)
            max_prod = temp_max
            result = max(result, max_prod)
        return result

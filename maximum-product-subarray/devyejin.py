from typing import List

# time O(n), space O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i] * max_prod, nums[i] * min_prod)
            max_prod, min_prod = max(candidates), min(candidates)
            result = max(result, max_prod)

        return result





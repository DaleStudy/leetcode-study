from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        prefix_product = 1
        for index in range(len(nums)):
            result[index] = prefix_product
            prefix_product *= nums[index]

        suffix_product = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= suffix_product
            suffix_product *= nums[index]

        return result
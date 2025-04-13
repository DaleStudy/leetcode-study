from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        products_except_self = [1] * array_length

        # First pass: multiply by all elements to the left
        left_product = 1
        for i in range(array_length):
            products_except_self[i] = left_product
            left_product *= nums[i]

        # Second pass: multiply by all elements to the right
        right_product = 1
        for i in range(array_length - 1, -1, -1):
            products_except_self[i] *= right_product
            right_product *= nums[i]

        return products_except_self

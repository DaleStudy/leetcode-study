from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        left_product = 1
        for i in range(len(nums) - 1):
            left_product *= nums[i]
            answer[i + 1] *= left_product
        right_product = 1
        for i in range(len(nums) - 1, 0, -1):
            right_product *= nums[i]
            answer[i - 1] *= right_product
        return answer

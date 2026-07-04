# 문제: https://leetcode.com/problems/product-of-array-except-self/
# 해설: https://www.algodale.com/problems/product-of-array-except-self/
# 위치: https://github.com/DaleStudy/leetcode-study/tree/main/product-of-array-except-self

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            answer[i] *= right
            right *= nums[i]

        return answer


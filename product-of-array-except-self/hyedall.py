"""
# https://leetcode.com/problems/product-of-array-except-self/description/

시간 복잡도 : O(n)
공간 복잡도 : O(1) (정답 배열 제외)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        answer = [1] * size

        prefix = 1
        for i in range(size):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(size)):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

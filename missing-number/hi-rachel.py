"""
TC: O(n)
SC: O(n)
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums)):
            if i not in num_set:
                return i
        return len(nums)


"""
TC: O(n log n)
SC: O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx != num:
                return idx
        return len(nums)


"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2 
        actual_sum = sum(nums)
        return expected_sum - actual_sum

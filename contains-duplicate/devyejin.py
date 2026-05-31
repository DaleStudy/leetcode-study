from typing import List
"""
time complexity : O(n)
space complexity : O(n)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)


"""
    Time complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return len(nums_set) != len(nums)

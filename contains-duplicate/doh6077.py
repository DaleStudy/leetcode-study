# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store unique numbers from nums
        nums_set = set(nums)
        return len(nums_set) != len(nums)

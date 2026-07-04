# - 문제: https://leetcode.com/problems/contains-duplicate/
# - 해설: https://www.algodale.com/problems/contains-duplicate/

# 217. Contains Duplicate
# - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)


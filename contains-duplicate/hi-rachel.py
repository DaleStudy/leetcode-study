"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

TC: O(n)
SC: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        [Complexity]
        Time: O(n)
        Space: O(n)
        '''
        return (len(nums) != len(set(nums)))

        '''
        alternative:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
        '''

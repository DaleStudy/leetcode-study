"""
https://leetcode.com/problems/contains-duplicate/
"""

# Time complexity : O(n)
#

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortedArray = sorted(nums)
        for i in range(len(sortedArray)): 
            if i == len(sortedArray) - 1: 
                return False
            if sortedArray[i] == sortedArray[i + 1] :
                return True
        return False
"""
https://leetcode.com/problems/contains-duplicate/
"""

# Time complexity : O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortedArrary = sorted(nums)
        for i in range(len(sortedArrary)): 
            if i == len(sortedArrary) - 1: 
                return False
            if sortedArrary[i] == sortedArrary[i + 1] :
                return True
        return False
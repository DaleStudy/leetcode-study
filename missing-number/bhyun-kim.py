"""
268. Missing Number
https://leetcode.com/problems/missing-number/description/

Solution:
    - Sort the input list
    - For each index in the input list:
        - If the index is not equal to the element:
            - Return the index
    - Return the length of the input list

Time complexity: O(nlogn+n)
    - The sort function runs O(nlogn) times
    - The for loop runs n times

Space complexity: O(1)
    - No extra space is used
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return len(nums)
        
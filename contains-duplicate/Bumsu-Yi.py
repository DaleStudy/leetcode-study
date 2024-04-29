"""
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                return True
            my_dict[num] = 0

        return False

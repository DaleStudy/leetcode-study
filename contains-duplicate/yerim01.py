# Leetcode 217: https://leetcode.com/problems/contains-duplicate/description/
# Goal: Given an array of integers,
# return True if the array has duplicates or return False if all elements are distinct.
# Approach:
# - Use a hash set to track elements we have already seen.
# - Iterate through the array and if the current number already exists in the set, return True.
# - Otherwise, add the current number to the set.
# Time complexity: O(n)
# - We iterate through the array once.
# Space complexity: O(n)
# - We store all elements in the set in the worst case.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = set()

        for n in nums:
            if n not in h:
                h.add(n)
            else:
                return True
        return False

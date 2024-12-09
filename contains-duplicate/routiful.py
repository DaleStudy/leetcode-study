# FIRST WEEK

# Question : 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
#   The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
#   All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
#   1 <= nums.length <= 105
#   -109 <= nums[i] <= 109 

# Notes:
# Counts every elements(in the list) using 'count()' API. Luckily it is less than O(n) but maximum O(n)
# Makes Dict; the key is elements of the list. If the length of them are different, the list has duplicate elements. It is O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            d[n] = 1
        if len(d) != len(nums):
            return True
        return False

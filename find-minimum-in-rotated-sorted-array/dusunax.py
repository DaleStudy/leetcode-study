'''
# 153. Find Minimum in Rotated Sorted Array

## Time Complexity: O(n)
- min() iterates through all elements to find the smallest one.

## Space Complexity: O(1)
- no extra space is used.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return min(nums)

"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Solution: Binary Search
    - Find the center of the array
    - Divide the array into two parts
    - Compare the left and right values of each part
    - If these values are in increasing order, return the left value of the first part
    - Otherwise, find the minimum value of the left and right values of each part
    - If the minimum value is the left value of the first part, recursively call the function with the first part
    - Otherwise, recursively call the function with the second part

Time complexity: O(log n)
Space complexity: O(1)

"""


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        center = len(nums) // 2
        arr1, arr2 = nums[:center], nums[center:]

        arr1_left, arr1_right = arr1[0], arr1[-1]
        arr2_left, arr2_right = arr2[0], arr2[-1]

        if arr1_left < arr1_right < arr2_left < arr2_right:
            return arr1_left

        min_val = min(arr1_left, arr1_right)
        min_val = min(min_val, arr2_left)
        min_val = min(min_val, arr2_right)

        if min_val in [arr1_left, arr1_right]:
            return self.findMin(arr1)
        else:
            return self.findMin(arr2)

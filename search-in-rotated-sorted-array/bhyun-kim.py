"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array

Solution: Binary Search
    - Find the center of the array
    - Divide the array into two parts
    - Compare the left and right values of each part
    - If the target value is in the range of the left and right values of the first part, recursively call the function with the first part
    - If the target value is in the range of the left and right values of the second part, recursively call the function with the second part
    - If the first part is rotated, recursively call the function with the first part
    - Otherwise, recursively call the function with the second part
    - If the output is not -1, add the length of the first part to the output

Time complexity: O(log n)
    - The time complexity is the same as the time complexity of the binary search algorithm
Space complexity: O(n)
    - Store the divided array in two variables
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        center = len(nums) // 2
        arr1, arr2 = nums[:center], nums[center:]

        arr1_left, arr1_right = arr1[0], arr1[-1]
        arr2_left, arr2_right = arr2[0], arr2[-1]

        if arr1_left <= target <= arr1_right:
            output = self.search(arr1, target)

        elif arr2_left <= target <= arr2_right:
            output = self.search(arr2, target)

            if output != -1:
                output += len(arr1)

        elif arr1_right < arr1_left:
            output = self.search(arr1, target)
        else:
            output = self.search(arr2, target)

            if output != -1:
                output += len(arr1)
        return output

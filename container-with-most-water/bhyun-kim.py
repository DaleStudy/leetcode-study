"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water

Solution: Two Pointers
    - Use two pointers to traverse the list
    - Calculate the area between the two pointers
    - Update the maximum area
    - Move the pointer with the shorter height
    - Return the maximum area

Time complexity: O(n)
    - The two pointers traverse the list only once
Space complexity: O(1)
    - No extra space is used
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            shorter_height = min(height[left], height[right])
            distance = right - left
            area = shorter_height * distance
            max_area = max(area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

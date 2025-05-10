from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Find the maximum area that can form a container with the most water.

        Problem: Given n non-negative integers representing heights of vertical lines,
        find two lines that together with the x-axis forms a container that holds the most water.

        Approach:
        - Use two pointers technique starting from both ends of the array
        - Calculate area at each step and keep track of maximum
        - Move the pointer with smaller height inward (since it limits the container height)

        Proof of correctness:
        - Every time we move a pointer, the width decreases by 1.
        - Why we move the pointer with smaller height:
          1) If we keep the smaller height and move the taller pointer instead,
             the width decreases but the height remains limited by the smaller value,
             so the area will always decrease.
          2) However, if we move the pointer with smaller height, we might find a taller line.
             In this case, even though width decreases, height might increase enough
             to create a larger area.
        - This way, we examine all possible combinations that could give us the maximum area.
        - We only explore combinations that have the potential to create an area larger
          than the maximum we've found so far.

        Time Complexity: O(n) where n is the length of heights array
        Space Complexity: O(1) using constant extra space

        Args:
            heights: List of heights of the vertical lines

        Returns:
            Maximum water area that can be contained
        """
        max_area = 0  # Initialize the maximum area to 0
        left, right = 0, len(heights) - 1  # Start with leftmost and rightmost positions

        # Continue until the pointers meet
        while left < right:
            # Calculate width between current lines (difference in positions)
            width = right - left

            # Height is limited by the shorter line
            current_height = min(heights[left], heights[right])

            # Calculate current area and update max_area if larger
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Move the pointer with smaller height inward
            # (Moving the smaller one gives potential for larger area since
            # width will decrease but height might increase)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

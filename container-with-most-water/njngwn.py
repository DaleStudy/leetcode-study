class Solution:
    # Time Complexity: O(n), n: len(height)
    # Space Complexity: O(1)
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, w * h)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area

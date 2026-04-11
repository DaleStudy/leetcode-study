class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            new_area = min(height[left], height[right]) * (right - left)
            area = max(area, new_area)

        return area

# Time Complexity: O(n)
# Space Complexity: O(1)
# Hello

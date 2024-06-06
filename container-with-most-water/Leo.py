class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxWater = 0

        while left <= right:
            hori = right - left
            vert = min(height[left], height[right])
            maxWater = max(maxWater, hori * vert)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
        # TC: O(n) SC: O(1)

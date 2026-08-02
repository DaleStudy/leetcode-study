# 1) Use two pointers and move the smaller height inward and update the max area at every iteration.
# TC: O(N) where N is len(height)
# SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return max_area

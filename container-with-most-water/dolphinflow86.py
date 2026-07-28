# 1) Use two pointers and move the smaller height inward and update the max area at every iteration.
# TC: O(N) where N is len(height)
# SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_area = 0
        while left < right:
            min_height = height[left] if height[left] < height[right] else height[right]
            area = min_height * (right - left)
            if max_area < area: 
                max_area = area

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return max_area

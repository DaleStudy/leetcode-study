class Solution:
    def maxArea(self, height: List[int]) -> int:  
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
            if height[left] <= height[right]:
                left += 1            
            else:
                right  -= 1
        return max_area


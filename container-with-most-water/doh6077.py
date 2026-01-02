# 11. Container With Most Water

# Use two pointesr 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1 
        container = 0 

        while left < right:
            cal = ((right - left) * min(height[left], height[right]))
            container = max(container, cal)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return container 

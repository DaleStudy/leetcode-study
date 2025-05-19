"""
Time complexity O(n)
Space complexity O(1)

Two pointer
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e = 0, len(height) - 1
        area = 0 # max area
        while s < e:
            h = min(height[s], height[e])
            tmp = h * (e - s) # area at current iteration
            area = max(area, tmp)
            # move pointer
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        
        return area

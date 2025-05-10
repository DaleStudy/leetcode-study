"""
너비: e - s
높이: min(height[s], height[e])

넓이 = e - s * min(height[s], height[e])
"""

# TC: O(N^2), SC: O(1)
# 모든 경우의 수를 따져 가장 넓이가 크게 나오는 경우를 찾는 풀이 -> Time Limit Exceeded
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for s in range(len(height) - 1):
            for e in range(s + 1, len(height)):
                area = (e - s) * min(height[s], height[e])
                max_area = max(area, max_area)
        return max_area
    

# 투 포인터 풀이
# TC: O(N), SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        s, e = 0, len(height) - 1
        while s < e:
            area = (e - s) * min(height[s], height[e])
            max_area = max(area, max_area)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return max_area
    

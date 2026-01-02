# idea : two-pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            max_area = max(max_area, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area



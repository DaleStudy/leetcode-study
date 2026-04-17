class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 가장 멀리 떨어져 있으면서 높이가 비슷한 막대기?
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            left, right = height[i], height[j]
            area = min(left, right) * (j - i)
            if area > max_area:
                max_area = area
            if left < right:
                i += 1
            else:
                j -= 1
        return max_area

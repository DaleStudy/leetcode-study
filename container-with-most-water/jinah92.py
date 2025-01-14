# O(1) spaces, O(N) times
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height)-1

        while start != end:
            # start, end 포인터에서 물의 넓이 계산 및 최대값 계산
            max_area = max((end-start)*min(height[start], height[end]), max_area)
            if height[start] < height[end]:
                start += 1
            elif height[start] >= height[end]:
                end -= 1
        
        return max_area

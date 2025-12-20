class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start, end = 0, len(height)-1

        while start <= end:
            area = (end-start)*(height[start] if height[start]<height[end] else height[end])
            if area > answer:
                answer = area
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return answer
    

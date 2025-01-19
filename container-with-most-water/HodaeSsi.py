# 시간 복잡도 : O(n)
# 공간 복잡도 : O(1)
# 문제 유형 : Two Pointer
class Solution:
	def maxArea(self, height: List[int]) -> int:
		left, right = 0, len(height) - 1
		max_area = 0
		
		while left < right:
			max_area = max(max_area, (right - left) * min(height[left], height[right]))
			if height[left] < height[right]:
				left += 1
			else:
				right -= 1
		
		return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        max_size = 0
        for line in range(len(height)):
            if left >= right:
                break
            cur_size = (right - left) * min(height[left], height[right])
            if height[left] < height[right]: # 왼쪽이 작으면 left 이동
                left += 1
            else:
                right -= 1
            max_size = max(max_size, cur_size)
        return max_size

class Solution:
    def maxArea(self, height):
        def divide_and_conquer(left, right):
            if left >= right:
                return 0
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            return max(
                area,
                divide_and_conquer(left + 1, right),
                divide_and_conquer(left, right - 1)
            )
        return divide_and_conquer(0, len(height) - 1)

"""
# Approach
투포인터로 양 끝에서 물의 양을 계산해나갑니다.
더 낮은 height인 쪽의 포인터를 줄여나가는데, 높이가 같은 경우에는 양쪽 모두 포인터를 움직입니다.

# Complexity
height의 길이가 N일 때
- Time complexity: O(N)
- Space complexity: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        best = 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best

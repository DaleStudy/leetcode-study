"""
Solution: Brute Force
Time: O(n^2)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                w = j - i
                max_water = max(h * w, max_water)

        return max_water


"""
Solution: Two Pointer
    1) 포인터 이동은 left height, right height 중 작은 value를 가질 경우 이동
Time: O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_water = max(h * w, max_water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

# Time: O(N)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = 0
        l, r = 0, len(height)-1
        length = len(height)-1

        while l < r:
            if height[l] < height[r]:
                size = max(size, height[l] * length)
                l += 1
                length -= 1
            else:
                size = max(size, height[r] * length)
                r -= 1
                length -= 1
        return size
        
# TC: O(N)
# SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_height = max(height)
        ans = 0

        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))

            if ans > max_height * (r - l):
                return ans

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans


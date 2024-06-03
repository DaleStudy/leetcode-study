# TC : O(n)
# SC : O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_val = 0

        while low < high:
            val = min(height[low], height[high]) * (high - low)
            max_val = max(val, max_val)
            if height[low] < height[high]:
                low += 1
            elif height[low] > height[high]:
                high -= 1
            # increment low or decrement high
            else:
                low += 1

        return max_val

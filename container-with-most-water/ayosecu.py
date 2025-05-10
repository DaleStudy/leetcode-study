from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(height)
        - Space Complexity: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = float("-inf")

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

tc = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([0, 1], 0)
]        

sol = Solution()
for i, (h, e) in enumerate(tc, 1):
    r = sol.maxArea(h)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

"""
TC: O(n)
SC: O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_here = min_here = ans = nums[0]

        for x in nums[1:]:
            if x < 0:
                max_here, min_here = min_here, max_here
            max_here = max(x, max_here * x)
            min_here = min(x, min_here * x)
            ans = max(ans, max_here)
        return ans

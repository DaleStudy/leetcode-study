from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(1)
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (1 + n) * n // 2

        for num in nums:
            total -= num
        
        return total

tc = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
]

sol = Solution()
for i, (n, e) in enumerate(tc, 1):
    r = sol.missingNumber(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

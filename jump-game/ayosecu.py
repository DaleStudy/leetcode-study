from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(1)
    """
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, jump in enumerate(nums):
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + jump)
        return True

tc = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False)
]

sol = Solution()
for i, (n, e) in enumerate(tc, 1):
    r = sol.canJump(n)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

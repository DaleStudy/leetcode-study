from typing import List

class Solution:
    """
        - Time Complexity: O(n), n = len(nums)
        - Space Complexity: O(n), n = len(nums)
    """
    def rob(self, nums: List[int]) -> int:
        # DP Formation
        # money[0] = 0
        # money[1] = nums[0]
        # money[i+1] = max(money[i-1] + nums[i], money[i])

        money = [0] * (len(nums) + 1)
        money[1] = nums[0]
        for i in range(1, len(nums)):
            money[i+1] = max(money[i-1] + nums[i], money[i])
        
        return money[-1]

tc = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([1, 2, 0, 5, 10], 12)
    ]

for i, (nums, e) in enumerate(tc, 1):
    sol = Solution()
    result = sol.rob(nums)
    print(f"TC {i} is Passed!" if result == e else f"TC {i} is Failed! - Expected: {e}, Result: {result}")

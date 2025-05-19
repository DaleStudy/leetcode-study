from typing import List

class Solution:
    """
        - Time Complexity: O(n^2), n = len(nums)
        - Space Complexity: O(n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

tc = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1)  
]

sol = Solution()
for i, (nums, e) in enumerate(tc, 1):
    r = sol.lengthOfLIS(nums)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")

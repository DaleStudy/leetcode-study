"""
# Time Complexity: O(N)
- N개의 개수를 가지는 dp 리스트를 만들고, 이를 순회
# Space Compelexity: O(N)
- N개의 dp 리스트 저장
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(len(nums) - 2):
            dp[i + 2] = max(dp[i] + nums[i + 2], dp[i + 1])

        return max(dp[-2], dp[-1])

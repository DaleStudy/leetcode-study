# TC : O(n^2)
# SC : O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for cur in range(1, len(nums)):
            for pre in range(cur):
                if nums[pre] < nums[cur]:
                    dp[cur] = max(1 + dp[pre], dp[cur])
        return max(dp)

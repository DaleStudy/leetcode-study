# TC: L is the length of nums.
#   lengthOfLIS: O(L^2) - nested loops iterate through all previous elements for each position

# SC:
#   lengthOfLIS: O(L) - dp array of size L to store LIS ending at each index

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

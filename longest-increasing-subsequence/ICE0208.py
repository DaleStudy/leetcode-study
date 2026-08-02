class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] : i를 마지막으로 했을 때 가장긴 증가 부분수열
        dp = [0] * len(nums)

        for i in range(0, len(nums)):
            dp[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = nums[0]부터 nums[i]까지의 LIS 길이
        # 처음은 1
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # nums[i]가 더 큰 경우 길이 + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp) # 전체 중 최대
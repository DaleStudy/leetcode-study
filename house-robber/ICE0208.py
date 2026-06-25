class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0: nums[0]
        # 1: max(nums[0], nums[1])
        # 2: max(nums[0] + nums[2], nums[1])
        # n : max(dp[n-2] + nums[n], dp[n-1])

        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        
        return dp[len(nums) - 1]

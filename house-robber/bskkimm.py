class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [2,7,9,10,5,4]
        # No Consecutive robbing --> able to skip as many times as wanted

        # which one to add? --> dp 

        # dp[i], dp[i-1] + nums[i+1]
        if len(nums) == 1:
            return nums[0]
  

        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]

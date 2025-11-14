class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            nums = [0] + nums
            dp = [0 for _ in range(len(nums))]
            dp[1] = nums[1]
            for i in range(1, len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
            return dp[-1]
    

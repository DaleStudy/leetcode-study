class Solution(object):
    def rob(self, nums):
        if len(nums) == 1 :
            return nums[0]
        if len(nums) == 2 :
            return max(nums)
        dp = [0 for i in nums]
        for i in range(len(nums) - 1) :
            if dp[i] < nums[i] :
                    dp[i] = nums[i]
            for j in range(i + 2,  len(nums)) :
                s = dp[i] + nums[j]
                if dp[j] < s :
                    dp[j] = s
        return max(dp)
        

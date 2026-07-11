# dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
# time : O(n)
# space : O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        if len(nums) == 1:
            return dp[0]
        
        dp[1] = max(dp[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
        
        return dp[len(nums) - 1]





# dp[i] = max(dp[i-1], dp[i-2] + num[i])
# TC : O(n)
# SC : O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0]

        if len(nums) == 1:
            return dp[0]

        dp[1] = max(nums[0],nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(dp)

        

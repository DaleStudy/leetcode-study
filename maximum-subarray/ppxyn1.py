# idea : DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The solution must run in O(N^2) or better.
        '''
        1. Idea: Sorting + Two Pointers (x) — This problem does not allow changing the original order of the array.
        2. Subarrays (TLE) — O(N^3), too slow.
        3. DP (o)
        '''
        max_total = nums[0]
        total = nums[0]
        # dp = [0]*len(nums) 
        # dp[0] = nums[0]
        for i in range(1,len(nums)):
            # dp[i] = max(nums[i], dp[i-1]+nums[i])
            total = max(nums[i], total+nums[i])
            max_total = max(total, max_total)
        return max_total 




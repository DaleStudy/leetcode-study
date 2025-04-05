# O(n) time, O(n) space

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]
    

# TS 코드
# function rob(nums: number[]): number {
#     if (nums.length === 0) return 0;
#     if (nums.length === 1) return nums[0];

#     const dp: number[] = new Array(nums.length).fill(0);
#     dp[0] = nums[0];
#     dp[1] = Math.max(nums[0], nums[1]);

#     for (let i = 2; i < nums.length; i++) {
#         dp[i] = Math.max(dp[i - 1], nums[i] + dp[i - 2]);
#     }

#     return dp[nums.length - 1];
# }

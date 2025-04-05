# O(n) time, O(n) space
# dp[i]는 i번째 집까지 봤을 때의 최대 누적 금액

# 두 가지 선택지를 고려:
# 1. 이 집을 턴다:
#    이전 집은 털 수 없으니 dp[i-2] + nums[i]
# 2. 이 집을 안 턴다:
#    그냥 전 집까지의 최대 금액 유지: dp[i-1]
# 두 가지 선택지 중 큰 걸 선택
# **dp[i] = max(dp[i-1], dp[i-2] + nums[i])**
# nums 길이가 2인 경우 range(2, 2)는 for문 안 돈다.

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

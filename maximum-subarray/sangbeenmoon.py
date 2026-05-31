# 30분 내로 풀지 못함.
# prefix sum 을 사용해서 풀어보려고 했으나 시간 초과.
# dp 문제임을 파악할 수 있는 직관 필요...

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)

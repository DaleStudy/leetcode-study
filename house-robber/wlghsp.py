"""
 * Time Complexity: O(N)
 * Space Complexity: O(N)
"""
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        # dp[i]: 0번 부터 i번째 집까지 고려했을 때 얻을 수 있는 최대 금액
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

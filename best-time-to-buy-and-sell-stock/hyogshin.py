class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 1)
        least_num = prices[0]
        for i in range(len(prices)):
            least_num = min(prices[i], least_num)
            dp[i] = max(prices[i] - least_num, dp[i-1])
        return max(dp)

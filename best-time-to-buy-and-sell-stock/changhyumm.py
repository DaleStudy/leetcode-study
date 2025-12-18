class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(0, len(prices) - 1):
            min_price = min(prices[i], min_price)
            profit = prices[i+1] - min_price
            max_profit = max(profit, max_profit)
        return max_profit
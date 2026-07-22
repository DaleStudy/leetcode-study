# 1) Keep track of local minimum and use local minimum to update max profile while interating prices.
# TC: O(N) where N is the length of prices
# SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

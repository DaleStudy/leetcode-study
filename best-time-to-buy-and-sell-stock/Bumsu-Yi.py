"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price - min_price
            min_price = min(min_price, price)
            max_profit = max(profit, max_profit)

        return max_profit

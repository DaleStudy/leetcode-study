"""
Time complexity O(n)
Space complexity O(1)

Dynamic programming
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)

        return max_profit

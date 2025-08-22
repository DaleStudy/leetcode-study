class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = float('inf')

        for price in prices:
            buy_price = min(buy_price, price)
            current_profit = price - buy_price
            max_profit = max(max_profit, current_profit)

        return max_profit

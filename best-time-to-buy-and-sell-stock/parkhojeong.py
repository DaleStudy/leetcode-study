class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10_000
        max_profit = 0
        for cur_price in prices:
            if max_profit < cur_price - min_price:
                max_profit = cur_price - min_price

            if cur_price < min_price:
                min_price = cur_price

        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10_000
        max_price = 0
        for cur_price in prices:
            if max_price < cur_price - min_price:
                max_price = cur_price - min_price

            if cur_price < min_price:
                min_price = cur_price

        return max_price

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = prices[0]
        temp_min = prices[0]
        diff = 0
        for price in prices:
            temp_diff = price - temp_min
            if temp_diff < 0:
                temp_min = price
            elif temp_diff > diff:
                max_price = price
                min_price = temp_min
                diff = temp_diff
            else:
                continue
        return diff


"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

1번 순회 -> O(n)

prices = [7,1,5,3,6,4]

price | min | max_profit
    7   |  7  |    0
    1   |  1  |    0
    5   |  1  |    4
    3   |  1  |    4
    6   |  1  |    5
    4   |  1  |    5

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
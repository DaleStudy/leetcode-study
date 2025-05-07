# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            prices를 순회하면서 다음을 트래킹하면 된다.
                (1) 지금까지의 최소 가격인 min_price 트래킹:    min(min_price, price)
                (2) 지금까지의 최대 수익인 max_profit 트래킹:   max(max_profit, price - min_price)
        """
        max_profit, min_price = 0, prices[0]

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(1)

        [Approach]
            two-pointer(buy, sell)로도 접근 가능하다.
            두 개의 pointer buy와 sell을 0, 1 인덱스에서 시작한 후, sell을 움직여가며 curr_profit = prices[sell] - prices[buy]를 구한다.
            그리고 curr_profit이 0보다 크면 max_profit을 트래킹하고, 그렇지 않으면 buy를 sell 위치로 당긴다.
            (curr_profit이 0보다 크지 않다는 것은, buy 시점의 price 이하인 price가 sell 시점에서 발견되었다는 뜻이다!)
        """
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit > 0:
                max_profit = max(max_profit, curr_profit)
            else:
                buy = sell
            sell += 1

        return max_profit

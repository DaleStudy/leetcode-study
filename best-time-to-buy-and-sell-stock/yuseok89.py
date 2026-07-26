# TC: O(N)
# SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_until_now = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - min_until_now

            if profit > max_profit:
                max_profit = profit

            if price < min_until_now:
                min_until_now = price

        return max_profit


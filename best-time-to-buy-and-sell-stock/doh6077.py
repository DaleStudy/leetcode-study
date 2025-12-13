
# 121. Best Time to Buy and Sell Stock
# O(n) - Two Pointers 
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0 
        right = 1
        profit = 0
        max_profit = 0 

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit

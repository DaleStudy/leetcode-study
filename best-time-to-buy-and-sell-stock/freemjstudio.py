# first attempt - time out

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            profit = max(prices[i:]) - prices[i]
            max_profit = max(max_profit, profit)
        return max_profit

# second attempt - greedy approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = prices[i] - min_price
            max_profit = max(max_profit, profit)
        return max_profit

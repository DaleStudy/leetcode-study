class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 10001 
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            if prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit

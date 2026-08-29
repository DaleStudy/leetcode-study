class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # set buy, sell as index of the prices
        buy = 0
        sell = 1

        max_profit = 0
        
        while sell < len(prices): # loop until we checked last prices
            if prices[buy] > prices[sell]:
                buy = sell # found low price for buying
            else :
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            
            sell += 1 # next sell price

        return max_profit
      

# Big-O 예측
# Time : O(n)
# Space : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if min_price > price:
                min_price = price
            
            profit = max(profit, price - min_price)
        return profit


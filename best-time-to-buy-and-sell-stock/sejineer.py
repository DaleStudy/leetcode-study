"""
시간 복잡도: O(N)
공간 복잡도: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        result = 0
        
        for price in prices:
            profit = price - buy
            buy = min(buy, price)
            result = max(profit, result)
        
        return result

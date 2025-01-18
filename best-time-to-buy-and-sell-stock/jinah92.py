# O(N) times, O(1) spaces
# price[i] 가격으로 팔아서 가장 수익을 많이 내려면, i-1번째까지 중 가장 값이 싼 날짜에서 주식을 사면 된다
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        
        return max_profit

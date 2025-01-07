"""
    TC : O(N)
        for문 한 번 => O(N)

    SC : O(1)
        변수 3개 선언 이외에 추가적으로 사용하는 메모리 없으므로
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        sell = prices[0]
        for price in prices:
            if price < buy:
                buy = price
                sell = price
            if price > sell:
                sell = price
            max_profit = max(max_profit, sell - buy)
        return max_profit

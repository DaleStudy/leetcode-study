# 시간 복잡도:
# - 배열을 한 번 순회하므로 O(n) (n은 prices 배열의 길이)

# 공간 복잡도:
# - 추가 변수 2개(min_price, max_profit)를 사용하므로 O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0

        for price in prices:
            if price < buy:
                buy = price
            else:
                profit = max(profit, price - buy)
        
        return profit

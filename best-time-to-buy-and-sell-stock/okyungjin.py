'''
[문제]
- 주식 가격이 담긴 정수 배열 prices가 주어진다.
- 특정 날짜에 주식을 단 한 번 구매하고, 미래의 특정 날짜에 판매하여 얻을 수 있는 최대 이익을 구한다.
- 이익을 낼 수 없는 경우 0을 반환하며, 반드시 구매 후 판매해야 한다.

[풀이]
1. prices 배열을 순회하며 최소 가격을 min_price에 기록한다.
2. 동시에 현재 가격에서 min_price를 뺀 이익이 최대인지 확인하여 갱신한다.
3. 최대 이익을 반환한다.

[복잡도]
시간 복잡도: O(N)
공간 복잡도: O(1)
'''
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit

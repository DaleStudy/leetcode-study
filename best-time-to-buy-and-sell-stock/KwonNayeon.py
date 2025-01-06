"""
Constraints:
1. 1 <= prices.length <= 10^5
2. 0 <= prices[i] <= 10^4

Time Complexity: O(n)

Space Complexity: O(1)

풀이 방법:
- 배열을 한 번 순회하면서:
   1. 현재까지의 최소 가격(min_price)을 계속 갱신
   2. 현재 가격에서 최소 가격을 뺀 값(현재 가능한 이익)과 기존 최대 이익을 비교하여 더 큰 값을 저장
- 이 방식으로 각 시점에서 가능한 최대 이익을 계산함

To Do:
- 다른 접근 방법 찾아보기 (Two Pointers, Dynamic Programming)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit


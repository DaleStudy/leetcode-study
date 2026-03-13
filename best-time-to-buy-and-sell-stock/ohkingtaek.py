class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
	지금까지 본 가격 중 가장 작은 값을 계속 저장하고
        현재 가격에서 그 최소값을 뺀 값으로 최대 이익을 갱신합니다.
        한 번 순회하면서 최대 profit을 찾는 방식입니다
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


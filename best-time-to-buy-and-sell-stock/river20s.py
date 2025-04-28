class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        주어진 prices를 한 번만 순회하면서
        지금까지의 최솟값을 추적하고, 
        '현재 가격 - 지금까지의 최솟값'으로 계산되는 이익이
        '지금까지의 최대 이익(초기 0)보다 크면 갱신하여 
        최종 최대 이익 구하기 문제
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_profit = 0 # 이익이 없을 때 0을 반환하게 초기화
        min_price = float('inf') # 최소 가격 저장, 무한대로 초기화해서 루프 첫 번째 가격부터 최소 가격에 저장

        for price in prices:
            # 최대 이익 갱신
            max_profit = max(max_profit, (price - min_price))
            # 최소 가격 갱신
            min_price = min(min_price, price)
            # 최소 이익 갱신 이후 최소 가격 갱신해야 함
            # 최대 이익 자체는 이미 '산' 주식에 대해 계산해야 하므로
            # 사는 동시 팔 수 없음

        return max_profit

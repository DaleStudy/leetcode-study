class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit: 최대 이익
        profit = 0

        # current_minimum: 현재까지의 최소 가격
        current_minimum = prices[0]

        # current_profit: 현재까지의 최대 이익
        current_profit = 0

        # 전체 배열에서 최솟값과, 최솟값 인덱스 이후 최댓값을 이익으로 계산하는 반복문
        for i in range(1, len(prices)):
            # 이익이 발생할 경우 현재 이익 갱신
            # 현재 이익을 갱신할 때마다 지금까지의 최대 이익도 갱신
            if prices[i] > current_minimum:
                current_profit = max(current_profit, prices[i] - current_minimum)
                profit = max(profit, current_profit)
            # 이익이 발생하지 않을 경우 최솟값 갱신
            else:
                current_minimum = prices[i]
        
        # 최대 이익만 저장되어 반환
        return profit

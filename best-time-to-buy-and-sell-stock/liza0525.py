# 시간 복잡도: O(n)
# - prices 배열을 한 번만 순회하도록 함

# 공간 복잡도: O(1)
# - 상수 위주로만 사용

class Solution:
    # 첫 날 이후 가격들을 순회하면서, 현재 가격으로 팔면 얼마나 수익나는지 계산하고
    # 최소 매수가(min_price)를 갱신하며 매수 가격을 최소화한다.
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # 지금까지 얻을 수 있었던 최대 수익
        min_price = prices[0]  # 지금까지 나온 가격 중 가장 낮은 값(최적의 매수 시점)

        for current_price in prices[1:]:
            # 현재 시점에서 팔면 얻을 수 있는 수익
            profit = current_price - min_price

            # 지금까지 본 수익 중 가장 큰 값으로 업데이트
            max_profit = max(max_profit, profit)

            # 최소 매수 가격 갱신 (더 낮은 가격이 나오면 바꿔준다)
            min_price = min(min_price, current_price)

        # 최종적으로 기록된 max_profit이 답
        return max_profit

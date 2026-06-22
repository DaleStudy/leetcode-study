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


# 7기 풀이
# 시간 복잡도: O(n)
#  - prices의 길이 n만큼 순회
# 공간 복잡도: O(1)
#  - 상수만 사용
class Solution:
    # 첫날부터 매일의 가격이 최소인지, 최대인지를 판단하여 가장 큰 이익을 낼 수 있는 값을 계산한다.
    # 첫날부터 시간 순서대로 확인해야 함(기간 중 가장 최댓값이 가장 최솟값보다 빠를 수도 있기 때문)
    def maxProfit(self, prices: List[int]) -> int:
        min_sell_price = 10 ** 4  # 문제 조건에서 10의 4승이 최대라고 하여 이를 min_sell_price의 초기값으로
        max_profit = 0

        for price in prices:
            # 매일 순회하며 지나간 시간들 중에 가장 작은 price인지 확인하여 업데이트
            min_sell_price = min(min_sell_price, price)

            # 매일 순회하며 오늘 얻을 수 있는 profit과 이전에 얻었던 max_profit을 비교하여 업데이트
            max_profit = max(max_profit, price - min_sell_price)

        return max_profit

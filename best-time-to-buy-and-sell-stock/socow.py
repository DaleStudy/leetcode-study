"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

문제: 주식 가격 배열이 주어질 때, 한 번 사고 한 번 팔아서 얻을 수 있는 최대 이익을 구하라.
     (매수는 매도보다 앞선 날짜여야 함)

예시:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5  (1일에 사서 4일에 팔면 6-1=5)
"""

from typing import List


# =============================================================================
# 풀이 1: 브루트 포스 (Brute Force)
# =============================================================================
# 아이디어: 모든 (매수일, 매도일) 조합을 확인하여 최대 이익을 찾는다.
# 시간 복잡도: O(n²) - 이중 반복문
# 공간 복잡도: O(1)
# 결과: Time Limit Exceeded (시간 초과)
# =============================================================================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        # i: 매수일 (0 ~ n-2)
        for i in range(len(prices) - 1):
            # r: 매도일 (i+1 ~ n-1), 매수일 이후여야 함
            for r in range(i + 1, len(prices)):
                # 현재 조합의 이익 = 매도가 - 매수가
                profit = prices[r] - prices[i]
                result = max(result, profit)

        return result


# =============================================================================
# 풀이 2: 한 번 순회 (One Pass) - 최적화
# =============================================================================
# 아이디어: 배열을 순회하면서 "지금까지의 최소 매수가"를 추적한다.
#          각 날짜에서 현재 가격으로 팔았을 때의 이익을 계산하고 최대값을 갱신한다.
#
# 핵심 통찰:
#   - 특정 날짜에 팔 때 최대 이익 = 현재가격 - (이전까지의 최소가격)
#   - 따라서 최소 가격만 추적하면 O(n)에 해결 가능
#
# 시간 복잡도: O(n) - 한 번 순회
# 공간 복잡도: O(1)
# =============================================================================
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0           # 최대 이익
        min_price = prices[0]    # 지금까지의 최소 매수가

        # 1일차부터 순회 (0일차는 min_price 초기값)
        for price in prices[1:]:
            # 오늘 팔았을 때의 이익 계산
            profit = price - min_price
            # 최대 이익 갱신
            max_profit = max(max_profit, profit)
            # 최소 매수가 갱신 (더 싼 날이 있으면 업데이트)
            min_price = min(min_price, price)

        return max_profit



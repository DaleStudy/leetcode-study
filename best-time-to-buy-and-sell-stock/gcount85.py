"""
# Approach
지금까지의 최저 가격을 갱신함과 동시에 최선의 이익도 업데이트합니다.

# Complexity
- Time complexity: O(N)

- Space complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        answer = 0

        for price in prices:
            min_price = min(min_price, price)
            answer = max(answer, price - min_price)

        return answer
